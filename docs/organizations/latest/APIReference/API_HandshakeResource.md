---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_HandshakeResource.html
---

# HandshakeResource
<a name="API_HandshakeResource"></a>

Contains additional details for a handshake.

## Contents
<a name="API_HandshakeResource_Contents"></a>

 ** Resources **   <a name="organizations-Type-HandshakeResource-Resources"></a>
An array of `HandshakeResource` objects. When needed, contains additional details for a handshake. For example, the email address for the sender.
Type: Array of [HandshakeResource](#API_HandshakeResource) objects
Required: No

 ** Type **   <a name="organizations-Type-HandshakeResource-Type"></a>
The type of information being passed, specifying how the value is to be interpreted by the other party:
+  **ACCOUNT**: ID for an AWS account.
+  **ORGANIZATION**: ID for an organization.
+  **EMAIL**: Email address for the recipient.
+  **OWNER\_EMAIL**: Email address for the sender.
+  **OWNER\_NAME**: Name of the sender.
+  **NOTES**: Additional text included by the sender for the recipient.
Type: String
Valid Values: `ACCOUNT | ORGANIZATION | ORGANIZATION_FEATURE_SET | EMAIL | MASTER_EMAIL | MASTER_NAME | NOTES | PARENT_HANDSHAKE | RESPONSIBILITY_TRANSFER | TRANSFER_START_TIMESTAMP | TRANSFER_TYPE | MANAGEMENT_ACCOUNT | MANAGEMENT_EMAIL | MANAGEMENT_NAME`
Required: No

 ** Value **   <a name="organizations-Type-HandshakeResource-Value"></a>
Additional information for the handshake. The format of the value string must match the requirements of the specified type.
Type: String
Required: No

## See Also
<a name="API_HandshakeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/HandshakeResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/HandshakeResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/HandshakeResource)
