---
source_url: https://docs.aws.amazon.com/keyspaces/latest/StreamsAPIReference/API_ValidationException.html
---

# ValidationException
<a name="API_ValidationException"></a>

The request validation failed because one or more input parameters failed validation.

This exception occurs when there are syntax errors in the request, field constraints are violated, or required parameters are missing. To help you fix the issue, the exception message provides details about which parameter failed and why.

HTTP Status Code returned: 400

## Contents
<a name="API_ValidationException_Contents"></a>

 ** errorCode **   <a name="keyspaces-Type-ValidationException-errorCode"></a>
An error occurred validating your request. See the error message for details.
Type: String
Valid Values: `InvalidFormat | TrimmedDataAccess | ExpiredIterator | ExpiredNextToken`
Required: No

 ** message **   <a name="keyspaces-Type-ValidationException-message"></a>
The input fails to satisfy the constraints specified by the service. Check the error details and modify your request.
Type: String
Required: No

## See Also
<a name="API_ValidationException_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspacesstreams-2024-09-09/ValidationException)
