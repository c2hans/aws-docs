---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_ConnectionSummary.html
---

# ConnectionSummary
<a name="API_ConnectionSummary"></a>

Summarized view of a [Connection](API_Connection.md) object.

## Contents
<a name="API_ConnectionSummary_Contents"></a>

 ** arn **   <a name="interconnect-Type-ConnectionSummary-arn"></a>
The ARN of the [Connection](API_Connection.md)
Type: String
Length Constraints: Minimum length of 59. Maximum length of 150.
Pattern: `arn:aws[a-z-]*:interconnect:[^:]+:[0-9]{12}:connection/(mcc|lmcc)-[a-z0-9]{8}`
Required: Yes

 ** attachPoint **   <a name="interconnect-Type-ConnectionSummary-attachPoint"></a>
The Attach Point to which the [Connection](API_Connection.md) should be associated.
Type: [AttachPoint](API_AttachPoint.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** bandwidth **   <a name="interconnect-Type-ConnectionSummary-bandwidth"></a>
The bandwidth of the [Connection](API_Connection.md)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `\d+[MG]bps`
Required: Yes

 ** description **   <a name="interconnect-Type-ConnectionSummary-description"></a>
A descriptive name of the [Connection](API_Connection.md)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[-a-zA-Z0-9_ ]+`
Required: Yes

 ** environmentId **   <a name="interconnect-Type-ConnectionSummary-environmentId"></a>
The [Environment](API_Environment.md) that this [Connection](API_Connection.md) is created on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** id **   <a name="interconnect-Type-ConnectionSummary-id"></a>
The identifier of the requested [Connection](API_Connection.md)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(mcc|lmcc)-[a-z0-9]{8}`
Required: Yes

 ** location **   <a name="interconnect-Type-ConnectionSummary-location"></a>
The provider specific location at the remote end of this [Connection](API_Connection.md)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** provider **   <a name="interconnect-Type-ConnectionSummary-provider"></a>
The provider on the remote end of this [Connection](API_Connection.md)
Type: [Provider](API_Provider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sharedId **   <a name="interconnect-Type-ConnectionSummary-sharedId"></a>
An identifier used by both AWS and the remote partner to identify the specific [Connection](API_Connection.md).
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** state **   <a name="interconnect-Type-ConnectionSummary-state"></a>
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

 ** type **   <a name="interconnect-Type-ConnectionSummary-type"></a>
The product variant supplied by this resource.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: Yes

 ** billingTier **   <a name="interconnect-Type-ConnectionSummary-billingTier"></a>
The billing tier this [Connection](API_Connection.md) is currently assigned.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 8.
Required: No

## See Also
<a name="API_ConnectionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/ConnectionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/ConnectionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/ConnectionSummary)
