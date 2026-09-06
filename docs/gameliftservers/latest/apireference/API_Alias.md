---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_Alias.html
---

# Alias
<a name="API_Alias"></a>

Properties that describe an alias resource.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_Alias_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AliasArn **   <a name="gameliftservers-Type-Alias-AliasArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers alias resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`. In a GameLift alias ARN, the resource ID matches the alias ID value.
Type: String
Pattern: `^arn:.*:alias\/alias-\S+`
Required: No

 ** AliasId **   <a name="gameliftservers-Type-Alias-AliasId"></a>
A unique identifier for the alias. Alias IDs are unique within a Region.
Type: String
Pattern: `^alias-\S+`
Required: No

 ** CreationTime **   <a name="gameliftservers-Type-Alias-CreationTime"></a>
A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Description **   <a name="gameliftservers-Type-Alias-Description"></a>
A human-readable description of an alias.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="gameliftservers-Type-Alias-LastUpdatedTime"></a>
The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** Name **   <a name="gameliftservers-Type-Alias-Name"></a>
A descriptive label that is associated with an alias. Alias names do not need to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** RoutingStrategy **   <a name="gameliftservers-Type-Alias-RoutingStrategy"></a>
The routing configuration, including routing type and fleet target, for the alias.
Type: [RoutingStrategy](API_RoutingStrategy.md) object
Required: No

## See Also
<a name="API_Alias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/Alias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/Alias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/Alias)
