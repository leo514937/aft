from __future__ import annotations

from typing import TypedDict

from ontology_audit_hub.domain.review.models import (
    GitHubRepoTarget,
    GitHubReviewPartialReport,
    GitHubReviewProgress,
    GitHubReviewRequest,
    GitHubReviewResponse,
)
from ontology_audit_hub.infra.github_snapshot import GitHubReviewCandidate, GitHubSnapshotFile
from ontology_audit_hub.infra.llm.github_review_agents import (
    GitHubReviewIssue,
    GitHubReviewScopePacket,
    GitHubReviewScopePlan,
    GitHubReviewStagePacket,
)


class GitHubReviewState(TypedDict, total=False):
    request: GitHubReviewRequest
    repo_target: GitHubRepoTarget | None
    snapshot_workspace_dir: str | None
    snapshot_dir: str | None
    candidate_files: list[GitHubReviewCandidate]
    focus_files: list[GitHubSnapshotFile]
    scope_packet: GitHubReviewScopePacket | None
    stage_packet: GitHubReviewStagePacket | None
    scope_plan: GitHubReviewScopePlan | None
    enabled_reviewers: list[str]
    correctness_issues: list[GitHubReviewIssue]
    risk_regression_issues: list[GitHubReviewIssue]
    security_issues: list[GitHubReviewIssue]
    test_coverage_issues: list[GitHubReviewIssue]
    merged_issues: list[GitHubReviewIssue]
    warnings: list[str]
    current_phase: str
    progress: GitHubReviewProgress | None
    partial_report: GitHubReviewPartialReport | None
    final_report: GitHubReviewResponse | None
