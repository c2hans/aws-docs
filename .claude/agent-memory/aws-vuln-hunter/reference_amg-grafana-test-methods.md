---
name: amg-grafana-test-methods
description: Reusable techniques and observed facts for live-testing Amazon Managed Grafana (AMG) v13 workspaces — provisioning, data-plane auth, SSRF/proxy, cross-account datasource, NAC
metadata:
  type: reference
---

Validated on the AMG v13.2 Grafana attack-plan run (2026-10-06, see [[agentcore-env]] for accounts/tooling).

**Provisioning a testable workspace (control plane, boto3 `grafana`):**
- `list_versions()` -> ['9.4','10.4','12.4','13.2']. v13 = `grafanaVersion='13.2'`.
- `create_workspace` with `accountAccessType='CURRENT_ACCOUNT'` REQUIRES `workspaceRoleArn` even for `permissionType='SERVICE_MANAGED'` (API differs from console). Create an IAM role trusting `grafana.amazonaws.com` first.
- Use `authenticationProviders=['SAML']` — you do NOT need a working IdP; service-account tokens work regardless of SAML status. Workspace reaches ACTIVE in ~4-6 min.
- Service accounts/tokens entirely via control plane: `create_workspace_service_account(grafanaRole='ADMIN'|'EDITOR'|'VIEWER')` then `create_workspace_service_account_token`. Token `key` is the `Authorization: Bearer` for the data plane at `https://<wsid>.grafana-workspace.<region>.amazonaws.com`.
- No SLR (`AWSServiceRoleForAmazonGrafana`) is created for a non-VPC workspace; no AMG-managed ENIs; no AMG-created Secrets Manager secrets. SLR managed policy has only EC2 ENI actions (no secretsmanager).

**Data-plane behavior observed (v13.2):**
- Legacy `/api/*` and new k8s-style `/apis/<group>.grafana.app/<ver>/namespaces/default/<resource>` enforce the SAME RBAC. `/apis` is role-aware: ADMIN responses carry `grafana.com/access/canReadSecrets` capability annotations VIEWER/EDITOR lack. Groups incl. secret.grafana.app (securevalues/keepers), provisioning (Git Sync), notifications.alerting, scim, banners, dashboard.
- Numeric-id datasource endpoints are DISABLED: `GET/DELETE /api/datasources/<n>` -> 404 even for ADMIN. The numeric-id PROXY `/api/datasources/proxy/<n>/...` is ALSO 404 (gone). Only `uid`/`name` and `/api/datasources/proxy/uid/<uid>/...` work.
- Datasource create/edit = ADMIN only (datasources:create/write). EDITOR 403. So the proxy-SSRF/url-swap primitive is Grafana-Admin-gated.
- Datasource proxy fetches the registered url server-side as `User-Agent: Grafana/13.2.x`, attaches configured `secureJsonData` creds in plaintext (e.g. basicAuth), and sends an `x-grafana-id` signed-identity JWT + `x-grafana-referer`. Link-local egress (169.254.169.254 IMDS, 169.254.170.2 ECS) is BLOCKED -> 403 "Access denied". Loopback 127.0.0.1:3000 (grafana itself) IS reachable (200).
- Legacy single-tenant alerting endpoints removed: `/api/alerts`, `/api/alert-notifications` -> 404. `/api/v1/provisioning/*` enforce role. `/api/alertmanager/grafana/api/v2/status` is viewer-readable but exposes only receiver NAMES/routing, no secret values.
- Team group-sync `POST /api/teams/:id/groups` requires `teams.permissions:write` (admin) — non-admin 403 on all teamIds.
- Plugin install `POST /api/plugins/:id/install` requires pluginAdminEnabled toggle (`update_workspace_configuration` plugins.pluginAdminEnabled) + `plugins:install` (admin). non-admin 403.

**NAC (network access control):** `update_workspace(networkAccessControl={'prefixListIds':[...], 'vpceIds':[]})` using an EC2 managed prefix list. Enforced from the REAL connection IP; `X-Forwarded-For`/`X-Real-IP`/underscore-variant spoofing does NOT bypass (403 Forbidden). Remove with `update_workspace(removeNetworkAccessConfiguration=True)` BEFORE data-plane teardown or your admin token is locked out.

**CONFIRMED finding — control-plane->data-plane privesc (L4c):** an IAM principal with ONLY `grafana:CreateWorkspaceServiceAccountToken` (no `grafana:*`, denied UpdateWorkspaceConfiguration) can mint a token for the ADMIN service account and gain full Grafana Admin (create admin SAs, read /api/admin/settings). No per-SA-role / resource / condition constraint on the action. Least-privilege trap, routing: account-operator.

**L11 designed TB7/TB8 stop:** CloudWatch datasource `jsonData.assumeRoleArn` -> role in account B (trusting A's workspace role) -> datasource health check (`GET /api/datasources/uid/<uid>/health`) returns "Successfully queried the CloudWatch metrics API" AND leaks the assumed-role ARN `arn:aws:sts::<B>:assumed-role/<role>/aws-go-sdk-...`. This is the cross-account STS reach = HARD STOP; it is DESIGNED/intended cross-account (operator config), not an isolation break. Workspace role needs sts:AssumeRole; B role needs to trust it.

**Plan reconciliation gotchas:** the plan's `AmazonGrafanaOrgAdminPolicy` (wildcard sts:AssumeRole) does NOT exist as an AWS-managed policy; the real org-admin policy is `AWSGrafanaAccountAdministrator` (grafana:* + iam:PassRole on * scoped to grafana.amazonaws.com, NO wildcard sts:AssumeRole).
