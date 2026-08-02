---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/responses.html
---

# Responses
<a name="responses"></a>

## Content of Responses
<a name="content-responses"></a>

Responses consist of a header and a body.

The header always contains two elements:
+ Content-Type: Set to application/xml.
+ Accept: Set to application/xml. For PUSH and POST requests only
+ The body consists of XML content. The body contains:
  + Unsuccessful request: a description of the error.
  + Successful POST or PUT request: the ID of the entity that was created or changed and a summary.
  + Successful GET request: the requested content.
  + Successful DELETE request: present but empty.

## Success Response
<a name="success-response"></a>

If a request is valid, Conductor Live returns the appropriate response:
+ For a POST, PUT or DELETE: A 200 OK response. The body may be empty or may contain XML content.
+ For a GET: A 200 OK response with XML content in the body.

## Error Response
<a name="error-response"></a>
+ If a request is not valid (for example, the request or the body are badly formatted), Conductor Live returns the appropriate HTTP response, typically an error in the 4xx or 5xx range.
+ If the URL of the request is invalid (for example, the IP address is wrong), then Conductor Live returns a 404 response.
+ If the request is valid (Conductor Live understands it), but the request cannot be fulfilled for some reason, then Conductor Live returns a 422 error.
