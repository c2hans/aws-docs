---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ProfileDetail.html
---

# ProfileDetail

The state of the profile after a read or write operation.

## Contents
<a name="API_ProfileDetail_Contents"></a>

 ** acceptRoleSessionName **   <a name="rolesanywhere-Type-ProfileDetail-acceptRoleSessionName"></a>
Used to determine if a custom role session name will be accepted in a temporary credential request.
Type: Boolean
Required: No

 ** aliasArn **   <a name="rolesanywhere-Type-ProfileDetail-aliasArn"></a>
The alias ARN of the profile, in the form `arn:partition:rolesanywhere:region:account:alias/profile/alias-name `. Present only if the profile has an alias.
You can use the alias ARN in place of the resource ID or ARN in the request parameters whose descriptions say that they accept an alias ARN. Don't use the alias ARN in AWS Identity and Access Management (IAM) policies. A policy statement that names an alias ARN doesn't apply to the resource that holds the alias. Write policies with the ARN that contains the resource ID instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:alias/profile/.*)`
Required: No

 ** aliasName **   <a name="rolesanywhere-Type-ProfileDetail-aliasName"></a>
The alias of the profile. Present only if the profile has an alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!.*//)([A-Za-z]([A-Za-z0-9_/-]*[A-Za-z0-9_-])?)?`
Required: No

 ** attributeMappings **   <a name="rolesanywhere-Type-ProfileDetail-attributeMappings"></a>
A mapping applied to the authenticating end-entity certificate.
Type: Array of [AttributeMapping](API_AttributeMapping.md) objects
Required: No

 ** createdAt **   <a name="rolesanywhere-Type-ProfileDetail-createdAt"></a>
The ISO-8601 timestamp when the profile was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="rolesanywhere-Type-ProfileDetail-createdBy"></a>
The AWS account that created the profile.
Type: String
Required: No

 ** durationSeconds **   <a name="rolesanywhere-Type-ProfileDetail-durationSeconds"></a>
 Used to determine how long sessions vended using this profile are valid for. See the `Expiration` section of the [CreateSession API documentation](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html#credentials-object) page for more details. In requests, if this value is not provided, the default value will be 3600.
Type: Integer
Required: No

 ** enabled **   <a name="rolesanywhere-Type-ProfileDetail-enabled"></a>
Indicates whether the profile is enabled.
Type: Boolean
Required: No

 ** managedPolicyArns **   <a name="rolesanywhere-Type-ProfileDetail-managedPolicyArns"></a>
A list of managed policy ARNs that apply to the vended session credentials.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** name **   <a name="rolesanywhere-Type-ProfileDetail-name"></a>
The name of the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[ a-zA-Z0-9-_]*`
Required: No

 ** previousAliasName **   <a name="rolesanywhere-Type-ProfileDetail-previousAliasName"></a>
The alias that the resource had before the update request. IAM Roles Anywhere returns this value only in the response to an update request that changed or removed an existing alias. It isn't returned when the alias was unchanged, when the resource had no alias before the request, or by other operations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!.*//)([A-Za-z]([A-Za-z0-9_/-]*[A-Za-z0-9_-])?)?`
Required: No

 ** profileArn **   <a name="rolesanywhere-Type-ProfileDetail-profileArn"></a>
The ARN of the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:profile/.*)`
Required: No

 ** profileId **   <a name="rolesanywhere-Type-ProfileDetail-profileId"></a>
The unique identifier of the profile.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`
Required: No

 ** requireInstanceProperties **   <a name="rolesanywhere-Type-ProfileDetail-requireInstanceProperties"></a>
Unused, saved for future use. Will likely specify whether instance properties are required in temporary credential requests with this profile.
Type: Boolean
Required: No

 ** roleArns **   <a name="rolesanywhere-Type-ProfileDetail-roleArns"></a>
A list of IAM roles that this profile can assume in a temporary credential request.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[^:]+)?:iam(:.*){2}(:role.*)`
Required: No

 ** sessionPolicy **   <a name="rolesanywhere-Type-ProfileDetail-sessionPolicy"></a>
A session policy that applies to the trust boundary of the vended session credentials.
Type: String
Required: No

 ** tipConfiguration **   <a name="rolesanywhere-Type-ProfileDetail-tipConfiguration"></a>
The trusted identity propagation (TIP) settings of the profile.
Type: [TipConfiguration](API_TipConfiguration.md) object
Required: No

 ** updatedAt **   <a name="rolesanywhere-Type-ProfileDetail-updatedAt"></a>
The ISO-8601 timestamp when the profile was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ProfileDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/ProfileDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/ProfileDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/ProfileDetail)
