---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_IngressPoint.html
---

# IngressPoint
<a name="API_IngressPoint"></a>

The structure of an ingress endpoint resource.

## Contents
<a name="API_IngressPoint_Contents"></a>

 ** IngressPointId **   <a name="sesmailmanager-Type-IngressPoint-IngressPointId"></a>
The identifier of the ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** IngressPointName **   <a name="sesmailmanager-Type-IngressPoint-IngressPointName"></a>
A user friendly name for the ingress endpoint resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[A-Za-z0-9_\-]+`
Required: Yes

 ** Status **   <a name="sesmailmanager-Type-IngressPoint-Status"></a>
The status of the ingress endpoint resource.
Type: String
Valid Values: `PROVISIONING | DEPROVISIONING | UPDATING | ACTIVE | CLOSED | FAILED | ASSOCIATED_VPC_ENDPOINT_DOES_NOT_EXIST`
Required: Yes

 ** Type **   <a name="sesmailmanager-Type-IngressPoint-Type"></a>
The type of ingress endpoint resource.
Type: String
Valid Values: `OPEN | AUTH | MTLS`
Required: Yes

 ** ARecord **   <a name="sesmailmanager-Type-IngressPoint-ARecord"></a>
 The DNS A Record that identifies your ingress endpoint. Configure your DNS Mail Exchange (MX) record with this value to route emails to Mail Manager.
Type: String
Required: No

## See Also
<a name="API_IngressPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/IngressPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/IngressPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/IngressPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
