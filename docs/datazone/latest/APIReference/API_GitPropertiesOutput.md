---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GitPropertiesOutput.html
---

# GitPropertiesOutput
<a name="API_GitPropertiesOutput"></a>

The properties of a Git connection returned by get and list operations, including connection status and any error details.

## Contents
<a name="API_GitPropertiesOutput_Contents"></a>

 ** codeConnectionArn **   <a name="datazone-Type-GitPropertiesOutput-codeConnectionArn"></a>
The ARN of the AWS CodeConnections connection used to connect to the Git repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[^:]*:(codeconnections|codestar-connections):[a-z0-9\-]+:\d{12}:connection/[a-f0-9\-]+`
Required: Yes

 ** defaultBranch **   <a name="datazone-Type-GitPropertiesOutput-defaultBranch"></a>
The default branch of the Git repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9._\-/]+`
Required: Yes

 ** repositoryId **   <a name="datazone-Type-GitPropertiesOutput-repositoryId"></a>
The ID of the Git repository. This is the owner and repository name, for example, owner/repo-name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9._\-]+(/[a-zA-Z0-9._\-]+)+`
Required: Yes

 ** errorMessage **   <a name="datazone-Type-GitPropertiesOutput-errorMessage"></a>
The error message that describes why the Git connection failed. This member is populated when the connection status is CREATE\_FAILED or UPDATE\_FAILED.
Type: String
Required: No

 ** status **   <a name="datazone-Type-GitPropertiesOutput-status"></a>
The status of the Git connection.
Type: String
Valid Values: `CREATING | CREATE_FAILED | DELETING | DELETE_FAILED | READY | UPDATING | UPDATE_FAILED | DELETED`
Required: No

## See Also
<a name="API_GitPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GitPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GitPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GitPropertiesOutput)
