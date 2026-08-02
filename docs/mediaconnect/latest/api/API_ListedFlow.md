---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedFlow.html
---

# ListedFlow
<a name="API_ListedFlow"></a>

 A summary of a flow, including its ARN, Availability Zone, and source type.

## Contents
<a name="API_ListedFlow_Contents"></a>

 ** availabilityZone **   <a name="mediaconnect-Type-ListedFlow-availabilityZone"></a>
 The Availability Zone that the flow was created in.
Type: String
Required: Yes

 ** description **   <a name="mediaconnect-Type-ListedFlow-description"></a>
 A description of the flow.
Type: String
Required: Yes

 ** flowArn **   <a name="mediaconnect-Type-ListedFlow-flowArn"></a>
 The ARN of the flow.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedFlow-name"></a>
 The name of the flow.
Type: String
Required: Yes

 ** sourceType **   <a name="mediaconnect-Type-ListedFlow-sourceType"></a>
 The type of source. This value is either owned (originated somewhere other than an MediaConnect flow owned by another AWS account) or entitled (originated at a MediaConnect flow owned by another AWS account).
Type: String
Valid Values: `OWNED | ENTITLED`
Required: Yes

 ** status **   <a name="mediaconnect-Type-ListedFlow-status"></a>
 The current status of the flow.
Type: String
Valid Values: `STANDBY | ACTIVE | UPDATING | DELETING | STARTING | STOPPING | ERROR`
Required: Yes

 ** maintenance **   <a name="mediaconnect-Type-ListedFlow-maintenance"></a>
 The maintenance settings for the flow.
Type: [Maintenance](API_Maintenance.md) object
Required: No

## See Also
<a name="API_ListedFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedFlow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedFlow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedFlow)
