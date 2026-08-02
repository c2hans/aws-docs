---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/include-request-expiration.html
---

# Include request expiration
<a name="include-request-expiration"></a>

This solution supports the expires query parameter, which is used to decide whether the Lambda should process a request. If an Expiry date is in the future, the request will be processed. If the Expiry date has already passed, the Lambda will return a 400 Bad Request error with the code: ImageRequestExpired.

Values in the expires query parameter are expected in the format: YYYYMMDDTHHmmssZ. For example: April 9th, 2024, at 10:30:15 UTC -4 would become 20240409T143015Z.

Request expiry is compatible with signatures, and should be included as part of the path when signing a request. For example:

```
const secret = '<YOUR_SECRET_VALUE_IN_SECRETS_MANAGER>';
const path = '/<YOUR_PATH>'; // Add the first '/' to path.
const expires = 'expires=<YOUR_EXPIRY>';
const to_sign = `${path}?${expires}`
const signature = crypto.createHmac('sha256', secret).update(to_sign).digest('hex');
```

**Note**
If the expires query parameter is being used in conjunction with any query parameter based edits. When generating a signature, please ensure that the query parameters are sorted. For more information, see .
