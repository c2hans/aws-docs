---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/token.html
---

# Token
<a name="token"></a>

 The main objective of token class is to generate unique tokens for the playback session. There are two main inputs of expected structure that determine the resulting token: **viewerAttributes** and **tokenPolicy**. **viewerAttributes** details the viewer specific inputs, which are the basis for calculating internal signature unique to that viewer. **tokenPolicy** defines a set of parameters which directly inform how the resulting token will be calculated by describing what attributes should be included in the token, what are the path patterns, expiry time and other relevant fields. Below are the examples that illustrate the structure of both objects that need to be supplied as an input:

 ***Viewer Attributes - Example***

```
{
"co": "GB",
"reg": "ENG",
"ip": "10.0.2.1",
"headers": {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; ...)",
"referer": "https://example.com/video1",
"x-auth": "uhfsdguyfde438t27gsda",
},
"qs": {
"m": "123456",
"filter": "mobile"
},
"sessionId": 'k1a12app2z'
}
```

|  Parameter  |  Default  |
| --- | --- |
|  co  |  viewer’s country as a two-letter code according to ISO-3166-1 alpha 2 standard  |
|  reg  |  region code that corresponds to viewer’s region. The value should match with the region codes of first-level subdivision of the ISO 3166-2 category  |
|  ip  |  viewer’s source IP address (either IPv4 or IPv6)  |
|  headers  |  set of request headers and their values that viewer must include in all the requests including the token  |
|  qs  |  set of query strings parameters and their values that viewer must include in all the requests including the token  |
|  sessionId  |  Explicit session ID value that would be associated to the token and signed. If you prefer sessionId to be auto-generated, omit this field  |

 ***Token Policy - Example***

```
{
"co": false,
"co_fallback": true,
"reg": false,
"reg_fallback": true,
"exc": [
"/tm/"
],
"exp": "+1h",
"headers": [
"user-agent",
"referer"
],
"querystrings": [
"m"
],
"ip": false,
"nbf": "1645000000",
"paths": [
"/v1/master/b3dae6b5505e7de150071442385b3f3817cfa640/",
"/v1/segment/b3dae6b5505e7de150071442385b3f3817cfa640/",
"/v1/manifest/b3dae6b5505e7de150071442385b3f3817cfa640/",
"/out/v1/df069e9593304746afc28eb0117f2dbd/"
],
"ssn": true,
"session_auto_generate": 12
}
```

|  Parameter  |  Default  |
| --- | --- |
|  co  |  a flag which determines whether viewer’s country attribute should be included in the token  |
|  co\_fallback  |  a flag instructing token validation function how to handle the request when country (co) is included in the token however it is not possible to verify viewer’s country when cloudfront-viewer-country header is missing. When set to true, request will be allowed in this scenario. When set to false request is blocked when viewer’s country can’t be determined.  |
|  reg  |  a flag which determines whether viewer’s country region attribute should be included in the token  |
|  reg\_fallback  |  a flag instructing token validation function how to handle the request when country (reg) is included in the token however it is not possible to verify viewer’s country region when cloudfront-viewer-country-region header is missing. When set to true, request will be allowed in this scenario. When set to false request is blocked when viewer’s country can’t be determined.  |
|  exc  |  List of the URL paths prefixes that should be excluded from the viewer attributes verification step. For any request which URL path starts with one of the URL paths listed in this property, only token integrity check, nbf timestamp and exp timer will be verified. This field allows to specify the URL path prefixes that would be subject to soft verification where it is known or likely that that not all the conditions can be met but access to this content should be still allowed (for instance advertisement segments requests)  |
|  exp  |  Mandatory attribute. Value determining how expiry time is set in the token. It can either be set as a relative time reference to the current time expressed in hours (for example, \+1h) or minutes (for example, \+30m). Alternatively, an absolute timestamp with second level precision can be set as well.  |
|  headers  |  List of viewer request headers subject to viewer attributes verification  |
|  querystrings  |  List of viewer request querystring parameters subject to viewer attributes verification  |
|  ip  |  a flag informing if source IP address should be included in the token  |
|  nbf  |  Timestamp indicating the time before which the access token must not be accepted for processing  |
|  paths  |  Mandatory attribute List of URL path prefixes the token can be used for. Unless viewer request matches with URL path included in exc property, URL must match with one of the paths in this property. The items on this list don’t specify the full URL path but just prefixes which spans from the beginning up to an arbitrary position in the URL path. each item in this list must be a substring of the actual viewer request URL to evaluate as a match.  |
|  ssn  |  A flag indicating whether session ID should be one of the inputs for token signature  |
|  session\_auto\_generate  |  If sessionId attribute is not present in viewerAttributes object, a number set in this property will set the length of the session ID to be automatically generated  |

*Object Properties*

**defaultTokenPolicy**: [object] → stores the default token policy object used in case a specific token policy is not provided as in input when calling **generate** method.

**secret: [Secret]** → reference to the instance of the Secret class, that provides the signing keys for the token generation process.

*Constructor*

**Token(secret: Secret, defaultTokenPolicy: object = null) →** constructor function maps the provided inputs (id, suspicion\_score) to the object attributes

*Instance Methods*

**generate(viewer\_attributes: object, playback\_url: string = null, token\_policy: object = self.defaultTokenPolicy, key\_alias: string = ‘primary’)** *returns string* → generate a token and returns either as a string which represents secure access token. If playback\_url is provided, the function returns modified URL with resulting string inserted. In that function Session class is used internally to generate **sessionId** in case it wasn’t provided explicitly in viewer\_attributes object as an input.

*How the session ID is derived if token policy **ssn** flag is set to true?* Order of precedence is as follows:
+  explicit **sessionId** value from viewer\_attributes input
+  auto generated using session\_auto\_generate value from token policy: new Session(viewer\_policy.session\_auto\_generate, true)
+  auto generated with the default session length of 12 characters

*Determining querystring parameter value used when generating a token.*

When a querystring parameter is listed in querystrings property in token policy, the value of which is later used when calculating a signature related to viewer attributes, **generate** method looks up its value in a following order:
+  playback\_url input parameter when **generate** method is called
+  viewer attributes querystring object
