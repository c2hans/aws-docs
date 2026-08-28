---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/create-vpc-endoint-policy.html
---

# Create a VPC endpoint policy for CodeArtifact
<a name="create-vpc-endoint-policy"></a>

 To create a VPC endpoint policy for CodeArtifact, specify the following:
+  The principal that can perform actions.
+  The actions that can be performed.
+  The resources that can have actions performed on them.

 The following example policy specifies that principals in the account 123456789012 can call the `GetAuthorizationToken` API and fetch packages from a CodeArtifact repository.

```
{
  "Statement": [
    {
      "Action": [
        "codeartifact:GetAuthorizationToken",
        "codeartifact:GetRepositoryEndpoint",
        "codeartifact:ReadFromRepository",
        "sts:GetServiceBearerToken"
      ],
      "Effect": "Allow",
      "Resource": "*",
      "Principal": {
         "AWS": "arn:aws:iam::123456789012:root"
       }
    }
  ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
