---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/quick-suite-access-approach/configuring-iam-policies.html
---

# Configuring IAM policies for Quick access
<a name="configuring-iam-policies"></a>

For more information about how AWS Identity and Access Management (IAM) policies work, see [Amazon Quick policies (identity-based)](https://docs.aws.amazon.com/quicksuite/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies) in the Quick documentation, and see [Policies and permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the IAM documentation. For sample policies for Quick, see [IAM policy examples for Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-policy-examples.html).

Note the following actions when configuring policies that allow users to self-provision access:
+ `quicksight:CreateReader` allows a user to self-provision read-only access in Quick. For more information, see [Self-provisioning an Amazon Quick read-only user](https://docs.aws.amazon.com/quicksuite/latest/userguide/provisioning-users.html#self-service-read-only-users).
+ `quicksight:CreateUser` allows a user to self-provision author access in Quick. For more information, see [Self-provisioning an Amazon Quick author](https://docs.aws.amazon.com/quicksuite/latest/userguide/provisioning-users.html#self-service-access).
+ `quicksight:CreateAdmin` allows a user to self-provision administrative access in Quick. For more information, see [Self-provisioning an Amazon Quick administrator](https://docs.aws.amazon.com/quicksuite/latest/userguide/provisioning-users.html#assigning-the-admin).
