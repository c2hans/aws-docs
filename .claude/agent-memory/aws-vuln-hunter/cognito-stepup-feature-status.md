---
name: cognito-stepup-feature-status
description: Cognito step-up ACR/AMR feature is API-modeled but not functionally deployed in the test accounts as of 2026-10-06
metadata:
  type: project
---

The Amazon Cognito **step-up authentication / ACR-AMR** surface (`AcrConfiguration` on
Create/UpdateUserPool, `AcrMapping` on Create/UpdateIdentityProvider, `TARGET_ACR_VALUES`/`MAX_AGE`
in the USER_AUTH flow, `acr_values`/`max_age` on managed login) was tested live on 2026-10-06
(run id 2026-10-06-3) and found **API-modeled but NOT functionally deployed** in accounts
183174222929 / 289531347876.

Observed (all boto3, botocore 1.43.108):
- botocore model has the shapes (`AcrConfigurationType`, `AcrLevelConfigType.AcrValue`, `AcrMappingType`, `UserPoolTierType=LITE/ESSENTIALS/PLUS`).
- Syntactic pattern validation runs at the model layer (AcrValue with a space -> InvalidParameterException "1 validation error detected").
- But: `AcrConfiguration` set at Create/UpdateUserPool reads back **null** in us-east-1, us-west-2, eu-west-1, us-east-2, ap-southeast-1 (not persisted).
- Documented uniqueness constraint NOT enforced: duplicate L1==L2 and L1=default-L4-URI both accepted (because the field is inert, not a real validation bypass).
- No `acr`/`amr` claims appear in ID or access tokens on USER_AUTH even with `TARGET_ACR_VALUES=urn:cognito:loa:4`.
- `TARGET_ACR_VALUES=loa:4` with only a password did NOT error (doc says it must) and on **LITE** tier did NOT raise `FeatureUnavailableInTierException` (doc line 147 says it must) — the whole backend path is absent.

**Why:** the entire attack plan's preconditions depend on `acr`/`amr` being issued and bound to real auth events; none of that is live, so Areas 1/2/4 are precondition-blocked, not refutable-as-safe.
**How to apply:** before re-running any ACR/AMR step-up hunt against these accounts, re-check deployment with the cheap discriminators above (AcrConfiguration persistence + LITE-tier FeatureUnavailableInTierException). Don't spend budget standing up domains/hosted-UI/canary OIDC IdPs until a token actually carries an `acr` claim. See [[env-sessions]].

Independently verified (feature-independent, documented-correct) behavior:
- Refresh token does NOT reset `auth_time` (iat advances, auth_time preserved) — Area 3 freshness bypass refuted.
- `email_verified` is non-mutable via SignUp and via self access-token UpdateUserAttributes — Area 5 mass-assignment refuted.
- `IssuerConfiguration` is only a `Type` enum (ORIGINAL/UPDATED issuer-URL format toggle), not an arbitrary custom `iss` — no iss-spoofing surface.
