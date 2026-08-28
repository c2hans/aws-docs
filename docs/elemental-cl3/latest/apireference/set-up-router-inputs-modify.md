---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-modify.html
---

# PUT: Modify a Router Input
<a name="set-up-router-inputs-modify"></a>

Modify the attributes of the specified input on the specified router. If, after the initial setup, you ever change the cabling on the input side of your router, you must use PUT Router Input to reflect these changes.

## HTTP Request and Response
<a name="set-up-router-inputs-modify-http-request-response"></a>

### Request URL
<a name="set-up-router-inputs-modify-http-request-response-url"></a>

```
PUT http://<Conductor IP address>/routers/<ID of router>/inputs/<ID of input>
```

### Call Header
<a name="set-up-router-inputs-modify-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-router-inputs-modify-http-request-response-request-body"></a>

The body contains only the elements to change. For a list of all elements, see [POST: Create a Router](set-up-routers-create.md)

## Example
<a name="set-up-router-inputs-modify-example"></a>

This request changes the router input number (the number of the physical input port on the router) to 4. The number 3 at the end of the example URL is the id assigned by Conductor Live when this input was created in the software. This input belongs to the router with the ID of 2.

This change would only be made to fix an error in the original setup or to reflect a change in the cabling (so that the router’s 4th input is now being used).

```
PUT http://198.51.100.0/routers/2/inputs/3
------------------------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<input>
  <input_id>4</input_id>
</input>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
