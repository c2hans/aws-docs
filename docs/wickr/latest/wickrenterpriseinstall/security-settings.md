---
source_url: https://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/security-settings.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Security settings
<a name="security-settings"></a>

AWS Wickr Enterprise provides configuration settings to enforce an enhanced security context for your deployment. This higher security standard is applied at the pod and container level, and is required for compliance with the Security Technical Implementation Guide (STIG).

Set the following configuration parameters to enforce the enhanced security context:

```
podSecurityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault
containerSecurityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop: ["ALL"]
```

**Warning**
For Opensearch, this security configuration disables the `fsgroup-volume` initContainer that updates permissions on the persistent storage, which can cause compatibility issues related to permissions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
