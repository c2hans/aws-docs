---
name: observabilityadmin-lambdaweb
description: CloudWatch observabilityadmin DatasetIntegration cross-account guards (confused-deputy + ARN IDOR both REFUTED) and Lambda WebFunction (lambda-web) plane NOT served — all B leads DOC-GAP
metadata:
  type: reference
---

Live run 2026-10-07 vs [[env-sessions]] (default=183174222929 attacker A, awsbb2=289531347876 victim B). botocore 1.43.108 has `observabilityadmin` (api 2018-05-10, endpoint via apigw, suffix cloudwatch) and `lambda-web`/`lambda-core`/`lambda-microvms` (all signing_name `lambda`, host lambda.<region>.amazonaws.com).

**observabilityadmin DatasetIntegration — clean isolation, two server-side account guards:**
- Resource model: ONE integration per account per region. ARN is fully deterministic: `arn:aws:observabilityadmin:us-east-1:<acct>:dataset-integration/default` (suffix literally `default`). CreateDatasetIntegration takes only `RoleArn`(+Tags); Get/Update/Delete take `Arn`.
- Cheap substrate: create a role trusting `logs.amazonaws.com` (+`test.logs.amazonaws.com` accepted too), inline any benign policy, then CreateDatasetIntegration(RoleArn=that). No build/compute.
- **A1 confused-deputy REFUTED (service-side):** CreateDatasetIntegration/UpdateDatasetIntegration with a cross-account RoleArn → `AccessDeniedException` 403 "Cross-account pass role is not allowed." The service forbids cross-account PassRole regardless of caller IAM (admin had iam:PassRole *). Confused deputy via logs.amazonaws.com cannot even be set up. The missing-aws:SourceAccount DOC-GAP is moot — no cross-account targeting possible.
- **A2 cross-account ARN IDOR REFUTED (service-side):** Get/Delete/Update on a foreign ARN → `ValidationException` 400 "Arn account does not match the caller's account." Fires BEFORE any resource lookup; IDENTICAL for a real-foreign ARN and a bogus-foreign suffix → NO ownership-vs-existence / enumeration oracle. Authz bound to caller account via ARN parse.
- **A3 test.logs.amazonaws.com — informational:** a same-account role trusting `test.logs.amazonaws.com` is accepted in CreateDatasetIntegration trust. No cross-account path (A1 guard), no fleet identity returned → no hard stop. Not a boundary cross.
- No scoped-principal retest needed: every crossing FAILED under AdministratorAccess, so a scoped principal fares no better.

**Lambda WebFunction (lambda-web) — NOT DEPLOYED/served → B1-B5 all DOC-GAP:**
- Every lambda-web op (ListWebFunctions, GetWebAccountSettings, Create*, raw SigV4 GET /2025-03-07/web-functions) → HTTP 403 `AccessDeniedException "Unable to determine service/operation name to be authorized"` (XML, not JSON) in us-east-1/us-west-2/us-east-2/eu-west-1/ap-southeast-2, BOTH accounts. The Lambda edge doesn't route these paths — model exists in botocore (uid lambda-web-2025-03-07) but the WebFunction control plane is not served for these accounts/regions. Uniform across regions = service-availability gate, not an account opt-in (no Create path to enable).
- **B1 managed policy `AWSLambdaInvokeWebFunctionEndpointAccess` is real & verbatim** (v1): `Allow lambda:InvokeWebFunctionEndpoint` on `arn:aws:lambda:*:*:web-function/*/endpoint/*` — wildcard account+region, no auth-type condition. iam SimulateCustomPolicy → `allowed` for a cross-account endpoint ARN (identity side open). BUT lambda-web control plane exposes `PutResourcePolicy`/`GetResourcePolicy` on web-function/endpoint resources — strong signal that cross-account invoke is ALSO resource-policy gated (classic Lambda pattern). So the wildcard identity grant alone is NOT a blast-radius-wide defect unless the resource-policy gate is absent — UNOBSERVABLE here because no endpoint can be created. B1 = DOC-GAP, not confirmable.
- B2 (ApplicationManaged anonymous ingress), B3 (build-plane SSRF/fleet identity — never reached, no hard stop), B4 (MultiRegion DomainName collision), B5 (ExecutionRoleArn/KmsKeyArn x-acct PassRole) — all blocked by the same unprovisionable plane. endpoint enum: authType ∈ {ApplicationManaged, IamAuth}; endpointType ∈ {HomeRegion, MultiRegion, PerRegion}.
- Also present/dark: `lambda-core` (NetworkConnector CRUD) and `lambda-microvms` (RunMicrovm/CreateMicrovmShellAuthToken etc.) — unexplored adjacent new Lambda surfaces, likely same availability gate.
