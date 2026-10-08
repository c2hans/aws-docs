---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_iot-data-plane_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS IoT data examples using AWS CLI
<a name="cli_2_iot-data-plane_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT data.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `delete-thing-shadow`
<a name="iot-data-plane_DeleteThingShadow_cli_2_topic"></a>

The following code example shows how to use `delete-thing-shadow`.

**AWS CLI**
**To delete a device's shadow document**
The following `delete-thing-shadow` example deletes the entire shadow document for the device named `MyRPi`.

```
aws iot-data delete-thing-shadow \
    --thing-name {{MyRPi}} \
    {{"output.txt"}}
```
The command produces no output on the display, but `output.txt` contains information that confirms the version and timestamp of the shadow document that you deleted.

```
{"version":2,"timestamp":1560270384}
```
For more information, see [Using Shadows](https://docs.aws.amazon.com/iot/latest/developerguide/using-device-shadows.html) in the *AWS IoT Developers Guide*.
+  For API details, see [DeleteThingShadow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/delete-thing-shadow.html) in *AWS CLI Command Reference*.

### `get-thing-shadow`
<a name="iot-data-plane_GetThingShadow_cli_2_topic"></a>

The following code example shows how to use `get-thing-shadow`.

**AWS CLI**
**To get a thing shadow document**
The following `get-thing-shadow` example gets the thing shadow document for the specified IoT thing.

```
aws iot-data get-thing-shadow \
    --thing-name {{MyRPi}} \
    {{output.txt}}
```
The command produces no output on the display, but the following shows the contents of `output.txt`:

```
{
  "state":{
    "reported":{
    "moisture":"low"
    }
  },
  "metadata":{
    "reported":{
      "moisture":{
        "timestamp":1560269319
      }
    }
  },
  "version":1,"timestamp":1560269405
}
```
For more information, see [Device Shadow Service Data Flow](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-data-flow.html) in the *AWS IoT Developers Guide*.
+  For API details, see [GetThingShadow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/get-thing-shadow.html) in *AWS CLI Command Reference*.

### `update-thing-shadow`
<a name="iot-data-plane_UpdateThingShadow_cli_2_topic"></a>

The following code example shows how to use `update-thing-shadow`.

**AWS CLI**
**To update a thing shadow**
The following `update-thing-shadow` example modifies the current state of the device shadow for the specified thing and saves it to the file `output.txt`.

```
aws iot-data update-thing-shadow \
    --cli-binary-format {{raw-in-base64-out}} \
    --thing-name {{MyRPi}} \
    --payload '{{{"state":{"reported":{"moisture":"okay"}}}}}' \
    {{"output.txt"}}
```
The command produces no output on the display, but the following shows the contents of `output.txt`:

```
{
    "state": {
        "reported": {
            "moisture": "okay"
        }
    },
    "metadata": {
        "reported": {
            "moisture": {
                "timestamp": 1560270036
            }
        }
    },
    "version": 2,
    "timestamp": 1560270036
}
```
For more information, see [Device Shadow Service Data Flow](https://docs.aws.amazon.com/iot/latest/developerguide/device-shadow-data-flow.html) in the *AWS IoT Developers Guide*.
+  For API details, see [UpdateThingShadow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/update-thing-shadow.html) in *AWS CLI Command Reference*.
