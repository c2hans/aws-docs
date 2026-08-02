---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-perimeter-for-amazon-bedrock/organizational-boundary-enforcement.html
---

# Organizational boundary enforcement
<a name="organizational-boundary-enforcement"></a>

## Control objective
<a name="control-objective.5d8e44ca-82b9-5b65-b560-83ec13f38eba"></a>

***Identity perimeter**** - Only trusted identities can access my resources*

Start by implementing organization-wide restrictions using the `aws:PrincipalOrgID` condition key to prevent any principal outside your AWS organization from accessing your Amazon Bedrock resources, even if they somehow obtain valid credentials. Apply the following policy as a service control policy (SCP) at the organization level to ensure consistent enforcement across all accounts.

**Important**
Replace `o-1234567890` with your actual AWS organization ID in all policy examples below. Find your organization ID by running: `aws organizations describe-organization`

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "RestrictToOrganization",
      "Effect": "Deny",
      "Action": "bedrock:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:PrincipalOrgID": "o-1234567890"
        },
        "Null": {
          "aws:PrincipalOrgID": "false"
        }
      }
    }
  ]
}
```

**Policy explanation:**
+ **RestrictToOrganization** - Denies all Amazon Bedrock operations from principals outside your AWS organization, creating a foundational security boundary that prevents external access even with valid credentials.

The null condition is crucial because it prevents bypass attempts where the `aws:PrincipalOrgID` key might be absent. This policy should be applied as a service control policy (SCP) at the organization level to ensure consistent enforcement across all accounts.
