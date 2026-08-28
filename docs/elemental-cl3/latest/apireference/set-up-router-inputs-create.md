---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-create.html
---

# POST: Create a Router Input
<a name="set-up-router-inputs-create"></a>

This request creates a new input for the specified router. Use this command repeatedly to set up all the router inputs. The total number of Router Input entities for a specified router must not exceed the `max_input `on that Router entity: it must not exceed the actual physical inputs on the router.

## HTTP Request and Response
<a name="set-up-router-inputs-create-http-request-response"></a>

### Request URL
<a name="set-up-router-inputs-create-http-request-response-url"></a>

```
POST http://<Conductor IP address>/routers/<ID of router>/inputs
```

### Call Header
<a name="set-up-router-inputs-create-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`
+ Content-Type: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Request Body
<a name="set-up-router-inputs-create-http-request-response-request-body"></a>

The response is in XML content consisting of one `input` element, consisting of the following elements.

| Element | Value | Description |
| --- | --- | --- |
| name | String | A name for this input, of your choosing. This name appears in the Inputs drop-down list on the Conductor Live web interface. |
| input\_number | Integer | The ID of the router input that you want to make known to Conductor Live. This is the ID for the input as assigned by the router (not assigned by AWS Elemental software).<br />When adding 4 Quadrant-4k inputs for HEVC, enter the first input number in the sequence. |
| input\_number\_end | Integer | When adding 4 Quadrant-4k inputs for HEVC, enter the last (fourth) input number in the sequence.<br />For example, if you provided “1” for input\_number, you would use “4” for input\_number\_end.<br />This element is not used if you are not adding 4 Quadrant-4k inputs. |
| quad | True/False | It is not necessary to specify this if you are not adding 4 Quadrant-4k inputs. |

### Response
<a name="set-up-router-inputs-create-http-request-response-response"></a>

The response repeats back the data that you posted with the addition of:
+ `id`: The newly assigned ID for the router\_input.
+ `router_id`: The router that this router input belongs to.

The response is identical to the response to a GET Router Input. See below for an example.

## Example
<a name="set-up-router-inputs-create-example"></a>

### Request
<a name="set-up-router-inputs-create-example-request"></a>

This request is to create a router input for the input that has the router-assigned ID of 1.

```
POST http://198.51.100.0/routers/2/inputs
-----------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
Accept:application/xml
-----------------------
<input>
  <name>Input 1</name>
  <input_number>1</input_number>
</input>
```

### Response
<a name="set-up-router-inputs-create-example-response"></a>

In this example, the router input has been automatically assigned the ID 4. The already existing ID of the router itself is 2.

```
<input>
      <id>4</id>
      <name>Input 1</name>
      <router_id>2</router_id>
      <input_number>1</input_number>
      <input_number_end nil="true"/>
      <quad>false</quad>
</input>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
