---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/csharp_kafka_code_examples.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Amazon MSK examples using SDK for .NET
<a name="csharp_kafka_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for .NET with Amazon MSK.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Serverless examples](#serverless_examples)

## Serverless examples
<a name="serverless_examples"></a>

### Invoke a Lambda function from an Amazon MSK trigger
<a name="serverless_MSK_Lambda_csharp_topic"></a>

The following code example shows how to implement a Lambda function that receives an event triggered by receiving records from an Amazon MSK cluster. The function retrieves the MSK payload and logs the record contents.

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-msk-to-lambda) repository.
Consuming an Amazon MSK event with Lambda using .NET.

```
using System.Text;
using Amazon.Lambda.Core;
using Amazon.Lambda.KafkaEvents;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace MSKLambda;

public class Function
{

    /// <param name="input">The event for the Lambda function handler to process.</param>
    /// <param name="context">The ILambdaContext that provides methods for logging and describing the Lambda environment.</param>
    /// <returns></returns>
    public void FunctionHandler(KafkaEvent evnt, ILambdaContext context)
    {

        foreach (var record in evnt.Records)
        {
            Console.WriteLine("Key:" + record.Key);
            foreach (var eventRecord in record.Value)
            {
                var valueBytes = eventRecord.Value.ToArray();
                var valueText = Encoding.UTF8.GetString(valueBytes);

                Console.WriteLine("Message:" + valueText);
            }
        }
    }

}
```
