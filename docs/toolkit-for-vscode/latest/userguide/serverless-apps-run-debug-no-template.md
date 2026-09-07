---
source_url: https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/serverless-apps-run-debug-no-template.html
---

# Running and debugging Lambda functions directly from code
<a name="serverless-apps-run-debug-no-template"></a>

When testing the AWS SAM application, you can choose to run and debug just the Lambda function and exclude other resources that the AWS SAM template defines. This approach involves using the [CodeLens](https://code.visualstudio.com/blogs/2017/02/12/code-lens-roundup) feature to identify Lambda function handlers in the source code that you can directly invoke.

The Lambda handlers that are detected by CodeLens depend on the language and runtime that you're using for your application.

|  Language/runtime | Criteria for Lambda functions to be identified by CodeLens indicators |
| --- | --- |
| C\# (dotnetcore2.1, 3.1; .NET 5.0) | The function has the following features:+  It's a public function of a public class. <br />+  It has one or two parameters. With two parameters, the second parameter must implement the `ILambdaContext` interface. <br />+  It has a `*.csproj` file in its parent folder within the VS Code workspace folder. The [ms-dotnettools.csharp extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) (or any extension that provides language symbols for C\#) is installed and enabled. |
| JavaScript/TypeScript (Node.js 12.x, 14.x) |  The function has the following features:+  It's an exported function with up to three parameters. <br />+  It has a `package.json` file in its parent folder within the VS Code workspace folder.   |
| Python (3.7, 3.8, 3.9, 3.10, 3.11, 3.12) |  The function has the following features:+  It's a top-level function. <br />+  It has a `requirements.txt` file in its parent folder within the VS Code workspace folder. The [ms-python.python extension](http://marketplace.visualstudio.com/items?itemName=ms-python.python) (or any extension that provides language symbols for Python) is installed and enabled. |
| Java (8, 8.al2, 11) |  The function has the following features:+  It's a public function of a public, non-abstract class. <br />+  It has one, two, or three parameters:   One parameter: Parameter can be anything.   Two parameters: Parameters must be a `java.io.InputStream` and a `java.io.OutputStream` OR the last parameter must be a `com.amazonaws.services.lambda.runtime.Context`.   Three parameters: Parameters must be a `java.io.InputStream` and a `java.io.OutputStream` AND the last parameter must be a `com.amazonaws.services.lambda.runtime.Context`.   <br />+  It has a `build.gradle` (Gradle) or `pom.xml` (Maven) file in its parent folder within the VS Code workspace folder. The [redhat.java extension](https://marketplace.visualstudio.com/items?itemName=redhat.java) (or any extension that provides language symbols for Java) is installed and enabled. This extension requires Java 11, no matter which Java runtime you're using.<br />The [vscjava.vscode-java-debug](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug) extension (or any extension that provides a Java debugger) is installed and enabled. |
| Go (1.x) |  The function has the following features:+  It's a top-level function. <br />+  It takes between 0 and 2 arguments. If there are two arguments, the first argument must implement `context.Context`. <br />+  It returns between 0 and 2 arguments. If there are more than 0 arguments, the last argument must implement `error`. <br />+  It has a `go.mod` file within the VS Code workspace folder. The [golang.go extension](https://marketplace.visualstudio.com/items?itemName=golang.Go) is installed, configured, and enabled. |

# To run and debug a serverless application directly from the application code

1. To view your application files in the VS Code File Explorer, choose **View**, **Explorer**.

1. From the application folder (for example, *my-sample-app*), expand the function folder (in this case, *hello-world*) and open the `app.js` file.

1. In the CodeLens indicator that identifies an eligible Lambda function handler, choose `Add Debug Configuration`.
![Access the Add Debug Configuration option in the CodeLens indicator for a Lambda function handler.](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/sam-codelens-lambda.png)

1. In the **Command Palette**, select the runtime in which your AWS SAM application will run.

1. In the editor for the `launch.json` file, edit or confirm values for the following configuration properties:
   + `"name"` – Enter a reader-friendly name to appear in the **Configuration** dropdown field in the **Run** view.
   + `"target"` – Ensure that the value is `"code"` so that a Lambda function handler is directly invoked.
   + `"lambdaHandler"` – Enter the name of the method within your code that Lambda calls to invoke your function. For example, for applications in JavaScript, the default is `app.lambdaHandler`.
   + `"projectRoot"` – Enter the path to the application file that contains the Lambda function.
   + `"runtime"` – Enter or confirm a valid runtime for the Lambda execution environment, for example, `"nodejs12.x"`.
   + `"payload"` – Choose one of the following options to define the event payload that you want to provide to your Lambda function as input:
     + `"json"`: JSON-formatted key-value pairs that define the event payload.
     + `"path"`: A path to the file that's used as the event payload.

     In the example below, the `"json"` option defines the payload.
![Configuring the launch.json file for directly invoking Lambda functions.](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/images/direct_invoke_config_updated_with_payload_field.png)

   For more information about these and other entries in the `launch.json` file, see [Configuration options for debugging serverless applications](serverless-apps-run-debug-config-ref.md).

1.

   If you're satisfied with the debug configuration, to start debugging, choose the green play arrow next to **RUN**.

   When the debugging sessions starts, the **DEBUG CONSOLE** panel shows debugging output and displays any values that the Lambda function returns. (When debugging AWS SAM applications, **AWS Toolkit** is selected as the **Output** channel in the **Output** panel.)
