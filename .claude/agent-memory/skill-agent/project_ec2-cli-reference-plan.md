---
name: ec2-cli-reference-plan
description: security-questionbuilder attack-research plan for the AWS CLI EC2 command reference (aws ec2, 1098 commands) in /work/aws-docs.
metadata:
  type: project
---

A boundary-first attack-research plan for the **AWS CLI `ec2` reference** (`https://docs.aws.amazon.com/cli/latest/reference/ec2/`, 1,098 subcommands) already exists — reuse/extend it, don't restart.

- Plan file: `/work/aws-docs/ec2-cli-reference-attack-research-plan.md` (identical copy at required outfile `/work/aws-docs/skill-agent_docs.aws.amazon.com_cli_latest_reference_ec2_.md`).
- Sub-agent raw notes: `_cli_subagent_ipam-byoip.md`, `_cli_subagent_capacity-governance.md`, `_cli_subagent_routeserver-mac-va.md`.
- The CLI reference is ~1:1 with the EC2 Query API, so it **cross-references** the existing API plan `skill-agent_docs.aws.amazon.com_AWSEC2_latest_APIReference_index.html.md` (§5A–5C: cross-account share/PassRole/KMS) instead of re-deriving it. The CLI plan's *net-new* content is (a) the CLI **client-layer** boundaries (`credential_process` code-exec, aliases/plugins, `--endpoint-url`, `--cli-input-json` hidden-param injection, `get-password-data` local decrypt) and (b) the **newest command clusters** the API plan predates.
- Top confirmed-doc leads: **B-Q1 (Critical)** IPAM `create-ipam-routing-policy-registration --force` = RPKI/BGP route-origin hijack primitive; **C-Q1** Verified Access `PolicyEnabled=false` possible fail-open authz bypass; **C-Q2/Q3** VA live OIDC trust-provider swap + `ClientSecret` plaintext export; **B-Q4** BYOASN message-replay; **A-Q1/A-Q3** Capacity-Manager/declarative-policies missing org-admin gate.

**Why:** part of the ongoing per-EC2-service documentation security-recon sweep in /work/aws-docs. **How to apply:** if asked to analyze the EC2 CLI surface again, extend this plan (esp. the carry-forward doc-gaps that need the VPC IPAM / Verified Access guides, not the CLI ref). See also [[ec2-instance-connect-plan]], [[aws-docs-see-also-injection]].
