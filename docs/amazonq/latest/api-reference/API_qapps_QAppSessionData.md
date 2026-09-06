---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QAppSessionData.html
---

# QAppSessionData
<a name="API_qapps_QAppSessionData"></a>

The response collected for a Amazon Q App session. This container represents a single response to a Q App session.

## Contents
<a name="API_qapps_QAppSessionData_Contents"></a>

 ** cardId **   <a name="qbusiness-Type-qapps_QAppSessionData-cardId"></a>
The card Id associated with the response submitted for a Q App session.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** user **   <a name="qbusiness-Type-qapps_QAppSessionData-user"></a>
The user who submitted the response for a Q App session.
Type: [User](API_qapps_User.md) object
Required: Yes

 ** submissionId **   <a name="qbusiness-Type-qapps_QAppSessionData-submissionId"></a>
The unique identifier of the submission.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: No

 ** timestamp **   <a name="qbusiness-Type-qapps_QAppSessionData-timestamp"></a>
The date and time when the session data is submitted.
Type: Timestamp
Required: No

 ** value **   <a name="qbusiness-Type-qapps_QAppSessionData-value"></a>
The response submitted for a Q App session.
Type: JSON value
Required: No

## See Also
<a name="API_qapps_QAppSessionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/QAppSessionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/QAppSessionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/QAppSessionData)
