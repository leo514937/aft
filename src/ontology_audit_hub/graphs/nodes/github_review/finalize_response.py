from __future__ import annotations

from ontology_audit_hub.domain.review.models import GitHubReviewResponse
from ontology_audit_hub.graphs.github_review_state import GitHubReviewState
from ontology_audit_hub.graphs.nodes.github_review._utils import build_local_report, to_domain_issue
from ontology_audit_hub.infra.llm.github_review_agents import GitHubReviewReport


def make_finalize_response_node():
    def finalize_response_node(state: GitHubReviewState) -> GitHubReviewState:
        report = state.get("final_report")
        if not isinstance(report, GitHubReviewReport):
            report = build_local_report(
                review_packet=state["review_packet"],
                issues=list(state.get("merged_issues", [])),
                warnings=list(state.get("warnings", [])),
            )

        reviewed_files = report.reviewed_files or [file.path for file in state["review_packet"].files]
        response = GitHubReviewResponse(
            summary=report.summary,
            issues=[to_domain_issue(issue) for issue in report.issues],
            reviewed_files=reviewed_files,
            warnings=list(dict.fromkeys(report.warnings or list(state.get("warnings", [])))),
            next_steps=list(dict.fromkeys(report.next_steps)),
        )
        return {
            **state,
            "final_report": response,
            "current_phase": "finalize_response",
        }

    return finalize_response_node
