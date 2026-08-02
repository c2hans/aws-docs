---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_TestGridSession.html
---

# TestGridSession
<a name="API_TestGridSession"></a>

A [TestGridSession](#API_TestGridSession) is a single instance of a browser launched from the URL provided by a call to [CreateTestGridUrl](API_CreateTestGridUrl.md).

## Contents
<a name="API_TestGridSession_Contents"></a>

 ** arn **   <a name="devicefarm-Type-TestGridSession-arn"></a>
The ARN of the session.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** billingMinutes **   <a name="devicefarm-Type-TestGridSession-billingMinutes"></a>
The number of billed minutes that were used for this session.
Type: Double
Required: No

 ** created **   <a name="devicefarm-Type-TestGridSession-created"></a>
The time that the session was started.
Type: Timestamp
Required: No

 ** ended **   <a name="devicefarm-Type-TestGridSession-ended"></a>
The time the session ended.
Type: Timestamp
Required: No

 ** seleniumProperties **   <a name="devicefarm-Type-TestGridSession-seleniumProperties"></a>
A JSON object of options and parameters passed to the Selenium WebDriver.
Type: String
Required: No

 ** status **   <a name="devicefarm-Type-TestGridSession-status"></a>
The state of the session.
Type: String
Valid Values: `ACTIVE | CLOSED | ERRORED`
Required: No

## See Also
<a name="API_TestGridSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/TestGridSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/TestGridSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/TestGridSession)
