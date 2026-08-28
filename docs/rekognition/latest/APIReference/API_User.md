---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_User.html
---

# User
<a name="API_User"></a>

Metadata of the user stored in a collection.

## Contents
<a name="API_User_Contents"></a>

 ** UserId **   <a name="rekognition-Type-User-UserId"></a>
 A provided ID for the User. Unique within the collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: No

 ** UserStatus **   <a name="rekognition-Type-User-UserStatus"></a>
 Communicates if the UserID has been updated with latest set of faces to be associated with the UserID.
Type: String
Valid Values: `ACTIVE | UPDATING | CREATING | CREATED`
Required: No

## See Also
<a name="API_User_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/User)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/User)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/User)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
