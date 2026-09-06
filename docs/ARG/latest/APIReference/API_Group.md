---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_Group.html
---

# Group
<a name="API_Group"></a>

A resource group that contains AWS resources. You can assign resources to the group by associating either of the following elements with the group:
+  [ResourceQuery](API_ResourceQuery.md) - Use a resource query to specify a set of tag keys and values. All resources in the same AWS Region and AWS account that have those keys with the same values are included in the group. You can add a resource query when you create the group, or later by using the [PutGroupConfiguration](API_PutGroupConfiguration.md) operation.
+  [GroupConfiguration](API_GroupConfiguration.md) - Use a service configuration to associate the group with an AWS service. The configuration specifies which resource types can be included in the group.

## Contents
<a name="API_Group_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GroupArn **   <a name="ARG-Type-Group-GroupArn"></a>
The Amazon resource name (ARN) of the resource group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: Yes

 ** Name **   <a name="ARG-Type-Group-Name"></a>
The name of the resource group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`
Required: Yes

 ** ApplicationTag **   <a name="ARG-Type-Group-ApplicationTag"></a>
A tag that defines the application group membership. This tag is only supported for application groups.
Type: String to string map
Key Pattern: `awsApplication`
Value Length Constraints: Minimum length of 12. Maximum length of 1600.
Value Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\.-]{1,150}/[a-zA-Z0-9]{22,26}`
Required: No

 ** Criticality **   <a name="ARG-Type-Group-Criticality"></a>
The critical rank of the application group on a scale of 1 to 10, with a rank of 1 being the most critical, and a rank of 10 being least critical.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** Description **   <a name="ARG-Type-Group-Description"></a>
The description of the resource group.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\sa-zA-Z0-9_\.-]*`
Required: No

 ** DisplayName **   <a name="ARG-Type-Group-DisplayName"></a>
The name of the application group, which you can change at any time.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Owner **   <a name="ARG-Type-Group-Owner"></a>
A name, email address or other identifier for the person or group who is considered as the owner of this application group within your organization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 300.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_Group_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/Group)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/Group)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/Group)
