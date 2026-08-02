---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/working-with-json.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# Work with JSON
<a name="working-with-json"></a>

JSON is a format for data exchange that is both human-readable and machine-readable. Although the name JSON is an acronym for *JavaScript Object Notation*, the format of JSON is independent of any programming language.

The AWS SDK for JavaScript uses JSON to send data to service objects when making requests and receives data from service objects as JSON. For more information about JSON, see [json.org](https://json.org).

![Showing the general format and parts of JSON.](http://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/images/json-format.png)

JSON represents data in two ways:
+ As an *object*, which is an unordered collection of name-value pairs. An object is defined within left (`{`) and right (`}`) braces. Each name-value pair begins with the name, followed by a colon, followed by the value. Name-value pairs are comma separated.
+ As an *array*, which is an ordered collection of values. An array is defined within left (`[`) and right (`]`) brackets. Items in the array are comma separated.

Here is an example of a JSON object that contains an array of objects in which the objects represent cards in a card game. Each card is defined by two name-value pairs, one that specifies a unique value to identify that card and another that specifies a URL that points to the corresponding card image.

```
var cards = [
  {"CardID":"defaultname", "Image":"defaulturl"},
  {"CardID":"defaultname", "Image":"defaulturl"},
  {"CardID":"defaultname", "Image":"defaulturl"},
  {"CardID":"defaultname", "Image":"defaulturl"},
  {"CardID":"defaultname", "Image":"defaulturl"}
];
```

## JSON as service object parameters
<a name="json-as-parameters-passed"></a>

Here is an example of simple JSON used to define the parameters of a call to an AWS Lambda service object.

```
const params = {
   FunctionName : funcName,
   Payload : JSON.stringify(payload),
   LogType : LogType.Tail,
};
```

The `params` object is defined by three name-value pairs, separated by commas within the left and right braces. When providing parameters to a service object method call, the names are determined by the parameter names for the service object method you plan to call. When invoking a Lambda function, `FunctionName`, `Payload`, and ` LogType` are the parameters used to call the `invoke` method on a Lambda service object.

When passing parameters to a service object method call, provide the JSON object to the method call, as shown in the following example of invoking a Lambda function.

```
const invoke = async (funcName, payload) => {
  const client = new LambdaClient({});
  const command = new InvokeCommand({
    FunctionName: funcName,
    Payload: JSON.stringify(payload),
    LogType: LogType.Tail,
  });

  const { Payload, LogResult } = await client.send(command);
  const result = Buffer.from(Payload).toString();
  const logs = Buffer.from(LogResult, "base64").toString();
  return { logs, result };
};
```
