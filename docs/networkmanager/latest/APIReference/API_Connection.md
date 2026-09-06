---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_Connection.html
---

# Connection
<a name="API_Connection"></a>

Describes a connection.

## Contents
<a name="API_Connection_Contents"></a>

 ** ConnectedDeviceId **   <a name="networkmanager-Type-Connection-ConnectedDeviceId"></a>
The ID of the second device in the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** ConnectedLinkId **   <a name="networkmanager-Type-Connection-ConnectedLinkId"></a>
The ID of the link for the second device in the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** ConnectionArn **   <a name="networkmanager-Type-Connection-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

 ** ConnectionId **   <a name="networkmanager-Type-Connection-ConnectionId"></a>
The ID of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** CreatedAt **   <a name="networkmanager-Type-Connection-CreatedAt"></a>
The date and time that the connection was created.
Type: Timestamp
Required: No

 ** Description **   <a name="networkmanager-Type-Connection-Description"></a>
The description of the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** DeviceId **   <a name="networkmanager-Type-Connection-DeviceId"></a>
The ID of the first device in the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** GlobalNetworkId **   <a name="networkmanager-Type-Connection-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** LinkId **   <a name="networkmanager-Type-Connection-LinkId"></a>
The ID of the link for the first device in the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-Connection-State"></a>
The state of the connection.
Type: String
Valid Values: `PENDING | AVAILABLE | DELETING | UPDATING`
Required: No

 ** Tags **   <a name="networkmanager-Type-Connection-Tags"></a>
The tags for the connection.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_Connection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/Connection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/Connection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/Connection)
