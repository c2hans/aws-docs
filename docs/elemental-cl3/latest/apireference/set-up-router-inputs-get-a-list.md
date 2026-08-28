---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/set-up-router-inputs-get-a-list.html
---

# GET List: Get a List of Router Inputs
<a name="set-up-router-inputs-get-a-list"></a>

Get the list of all the inputs for the specified router.

## HTTP Request and Response
<a name="set-up-router-inputs-get-a-list-http-request-response"></a>

### Request URL
<a name="set-up-router-inputs-get-a-list-http-request-response-url"></a>

```
GET http://<Conductor IP address>/routers/<ID of router>/inputs
```

### Call Header
<a name="set-up-router-inputs-get-a-list-http-request-response-call-header"></a>
+ Accept: Set to `application/xml`

If you are implementing user authentication, you must also include three authorization headers; see [Header Content for User Authentication](header-content-user.md).

### Response
<a name="set-up-router-inputs-get-a-list-http-request-response-response"></a>

The response is XML content consisting of one `inputs` element that contains:
+ An HREF attribute that specifies the product and version installed on the Conductor Live node.
+ Zero or more `input` elements, one for each input found. Each `input` element contains several elements.

| Element | Value | Description |
| --- | --- | --- |
| id | Integer | The ID for this input, unique for this router and assigned by AWS Elemental Conductor Live 3 when the input is created. |
| name | String | The name for this input. |
| router\_id | Integer | The router to which this input belongs. |
| input\_number | Integer | The ID of the router input corresponding to the physical port on the router. This number is assigned by the router and specified to Conductor Live by the user (not assigned by AWS Elemental software).<br />For 4 Quadrant-4k inputs, this is the first input number in a sequence of four. |
| input\_number\_end | Integer | For 4 Quadrant-4k inputs, the last input number in the sequence of four.<br />This element is not used if you are not adding 4 Quadrant-4k inputs. |
| quad | True/False | It is not necessary to specify if you are not adding 4 Quadrant-4k inputs. |

## Example
<a name="set-up-router-inputs-get-a-list-example"></a>

This request is for the inputs associated with the router with the ID 4. The response specifies that there are two inputs in this router with IDs 3 and 4.

```
GET http://198.51.100.0/routers/4/inputs
----------------------------
Content-type:application/vnd.elemental+xml;version=3.3.0
----------------------------
<?xml version="1.0" encoding="UTF-8"?>
<inputs href="/routers/4/inputs" product="AWS Elemental Conductor Live" version="3.3.nnnnn">
 <input>
    <id>3</id>
    <name>Input 1</name>
    <router_id>2</router_id>
    <input_number>1</input_number>
    <input_number_end nil="true"/>
    <quad>false</quad>
 </input>
 <input>
    <id>4</id>
    <name>Input 2</name>
    <router_id>2</router_id>
    <input_number>2</input_number>
    <input_number_end nil="true"/>
    <quad>false</quad>
 </input>
</inputs>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
