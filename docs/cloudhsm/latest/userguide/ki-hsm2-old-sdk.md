---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/ki-hsm2-old-sdk.html
---

# Known issues of operation failure using AWS CloudHSM client version 5.12.0 on hsm2.medium
<a name="ki-hsm2-old-sdk"></a>

The following issues impact AWS CloudHSM when using AWS CloudHSM client version 5.12.0

## Issue: Error during get-attribute operation
<a name="ki-hsm2-old-sdk-1"></a>

If you're migrating from hsm1.medium to hsm2m.medium and using CloudHSM Client SDK 5.12.0, you may observe errors related to attribute handling.

You might see the following error message in the client logs: `Error in deserialization of data: Invalid integer conversion`

**Impact: Below operations will fail using client version 5.12.0**
+ In PKCS\#11 SDK, calls to C\_GetAttributeValue fail
+ In CloudHSM CLI, the key list command shows no attributes in the output
+ In CloudHSM CLI, key generate-file may fail for keys generated using hsm1.medium

**Resolution: **We recommend upgrading to the latest version of the SDK which resolves this issue.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
