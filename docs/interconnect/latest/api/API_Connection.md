---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_Connection.html
---

# Connection
<a name="API_Connection"></a>

The object describing the provided connectivity from the AWS region to the partner location.

## Contents
<a name="API_Connection_Contents"></a>

 ** activationKey **   <a name="interconnect-Type-Connection-activationKey"></a>
The Activation Key associated to this conne[Connection](#API_Connection)ction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** arn **   <a name="interconnect-Type-Connection-arn"></a>
An ARN of a [Connection](#API_Connection) object.
Type: String
Length Constraints: Minimum length of 59. Maximum length of 150.
Pattern: `arn:aws[a-z-]*:interconnect:[^:]+:[0-9]{12}:connection/(mcc|lmcc)-[a-z0-9]{8}`
Required: Yes

 ** attachPoint **   <a name="interconnect-Type-Connection-attachPoint"></a>
The Attach Point to which the [Connection](#API_Connection) should be associated."
Type: [AttachPoint](API_AttachPoint.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** bandwidth **   <a name="interconnect-Type-Connection-bandwidth"></a>
The specific selected bandwidth of this [Connection](#API_Connection).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `\d+[MG]bps`
Required: Yes

 ** description **   <a name="interconnect-Type-Connection-description"></a>
A descriptive name for the [Connection](#API_Connection).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[-a-zA-Z0-9_ ]+`
Required: Yes

 ** environmentId **   <a name="interconnect-Type-Connection-environmentId"></a>
The specific [Environment](API_Environment.md) this [Connection](#API_Connection) is placed upon.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** id **   <a name="interconnect-Type-Connection-id"></a>
The short identifier of the connection object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(mcc|lmcc)-[a-z0-9]{8}`
Required: Yes

 ** location **   <a name="interconnect-Type-Connection-location"></a>
The provider specific location on the remote side of this [Connection](#API_Connection)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** ownerAccount **   <a name="interconnect-Type-Connection-ownerAccount"></a>
The account that owns this [Connection](#API_Connection)
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** provider **   <a name="interconnect-Type-Connection-provider"></a>
The provider on the remote side of this [Connection](#API_Connection).
Type: [Provider](API_Provider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sharedId **   <a name="interconnect-Type-Connection-sharedId"></a>
An identifier used by both AWS and the remote partner to identify the specific [Connection](#API_Connection).
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** state **   <a name="interconnect-Type-Connection-state"></a>
+  `requested`: The initial state of a connection. The state will remain here until the Connection is accepted on the Partner portal.
+  `pending`: The connection has been accepted and is being provisioned between AWS and the Partner.
+  `available`: The connection has been fully provisioned between AWS and the Partner.
+  `deleting`: The connection is being deleted.
+  `deleted`: The connection has been deleted.
+  `failed`: The connection has failed to be created.
+  `updating`: The connection is being updated.
Type: String
Valid Values: `available | requested | pending | down | deleting | deleted | failed | updating`
Required: Yes

 ** type **   <a name="interconnect-Type-Connection-type"></a>
The specific product type of this [Connection](#API_Connection).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: Yes

 ** billingTier **   <a name="interconnect-Type-Connection-billingTier"></a>
The billing tier this [Connection](#API_Connection) is currently assigned.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 8.
Required: No

 ** tags **   <a name="interconnect-Type-Connection-tags"></a>
The tags on the [Connection](#API_Connection)
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Connection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/Connection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/Connection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/Connection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Interconnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query interconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
