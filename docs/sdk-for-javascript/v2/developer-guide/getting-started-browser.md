---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/getting-started-browser.html
---

The AWS SDK for JavaScript v2 has reached end-of-support. We recommend that you migrate to [AWS SDK for JavaScript v3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/). For additional details and information on how to migrate, please refer to this [announcement](https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-aws-sdk-for-javascript-v2/).

# Getting Started in a Browser Script
<a name="getting-started-browser"></a>

![JavaScript code example that applies to browser execution](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/images/browsericon.png)

**This browser script example shows you:**
+ How to access AWS services from a browser script using Amazon Cognito Identity.
+ How to turn text into synthesized speech using Amazon Polly.
+ How to use a presigner object to create a presigned URL.

## The Scenario
<a name="getting-started-browser-scenario"></a>

Amazon Polly is a cloud service that converts text into lifelike speech. You can use Amazon Polly to develop applications that increase engagement and accessibility. Amazon Polly supports multiple languages and includes a variety of lifelike voices. For more information about Amazon Polly, see the [*Amazon Polly Developer Guide*](https://docs.aws.amazon.com/polly/latest/dg/).

The example shows how to set up and run a simple browser script that takes text you enter, sends that text to Amazon Polly, and then returns the URL of the synthesized audio of the text for you to play. The browser script uses Amazon Cognito Identity to provide credentials needed to access AWS services. You will see the basic patterns for loading and using the SDK for JavaScript in browser scripts.

**Note**
Playback of the synthesized speech in this example depends on running in a browser that supports HTML 5 audio.

![Illustration of how a browser script interacts with Amazon Cognito Identity and Amazon Polly services](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/images/browserscenario.png)

The browser script uses the SDK for JavaScript to synthesize text by using these APIs:
+ [`AWS.CognitoIdentityCredentials`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityCredentials.html) constructor
+ [`AWS.Polly.Presigner`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Polly/Presigner.html) constructor
+ [`getSynthesizeSpeechUrl`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Polly/Presigner.html#getSynthesizeSpeechUrl-property)

## Step 1: Create an Amazon Cognito Identity Pool
<a name="getting-started-browser-create-identity-pool"></a>

In this exercise, you create and use an Amazon Cognito identity pool to provide unauthenticated access to your browser script for the Amazon Polly service. Creating an identity pool also creates two IAM roles, one to support users authenticated by an identity provider and the other to support unauthenticated guest users.

In this exercise, we will only work with the unauthenticated user role to keep the task focused. You can integrate support for an identity provider and authenticated users later. For more information about adding a Amazon Cognito identity pool, see [Tutorial: Creating an identity pool](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-identity-pool.html) in the *Amazon Cognito Developer Guide*.

**To create an Amazon Cognito identity pool**

1. Sign in to the AWS Management Console and open the Amazon Cognito console at [https://console.aws.amazon.com/cognito/](https://console.aws.amazon.com/cognito/).

1. In the left navigation pane, choose **Identity pools**.

1. Choose **Create identity pool**.

1. In **Configure identity pool trust**, choose **Guest access** for user authentication.

1. In **Configure permissions**, choose **Create a new IAM role** and enter a name (for example, *getStartedRole*) in the **IAM role name**.

1. In **Configure properties**, enter a name (for example, *getStartedPool*) in **Identity pool name**.

1. In **Review and create**, confirm the selections that you made for your new identity pool. Select **Edit** to return to the wizard and change any settings. When you're done, select **Create identity pool**.

1. Note the **Identity pool ID** and the **Region** of the newly created Amazon Cognito identity pool. You need these values to replace {{IDENTITY\_POOL\_ID}} and {{REGION}} in [Step 4: Write the Browser Script](#getting-started-browser-write-sample).

After you create your Amazon Cognito identity pool, you're ready to add permissions for Amazon Polly that are needed by your browser script.

## Step 2: Add a Policy to the Created IAM Role
<a name="getting-started-browser-iam-role"></a>

To enable browser script access to Amazon Polly for speech synthesis, use the unauthenticated IAM role created for your Amazon Cognito identity pool. This requires you to add an IAM policy to the role. For more information about modifying IAM roles, see [Modifying a role permissions policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-modify_permissions-policy) in the *IAM User Guide*.

**To add an Amazon Polly policy to the IAM role associated with unauthenticated users**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, choose **Roles**.

1. Choose the name of the role that you want to modify (for example, *getStartedRole*), and then choose the **Permissions** tab.

1. Choose **Add permissions** and then choose **Attach policies**.

1. In the **Add permissions** page for this role, find and then select the check box for **AmazonPollyReadOnly**.
**Note**
You can use this process to enable access to any AWS service.

1. Choose **Add permissions**.

After you create your Amazon Cognito identity pool and add permissions for Amazon Polly to your IAM role for unauthenticated users, you are ready to build the webpage and browser script.

## Step 3: Create the HTML Page
<a name="getting-started-browser-create-html"></a>

The sample app consists of a single HTML page that contains the user interface and browser script. To begin, create an HTML document and copy the following contents into it. The page includes an input field and button, an `<audio>` element to play the synthesized speech, and a `<p>` element to display messages. (Note that the full example is shown at the bottom of this page.)

For more information on the `<audio>` element, see [audio](https://www.w3schools.com/tags/tag_audio.asp).

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>AWS SDK for JavaScript - Browser Getting Started Application</title>
  </head>

  <body>
    <div id="textToSynth">
      <input autofocus size="23" type="text" id="textEntry" value="It's very good to meet you."/>
      <button class="btn default" onClick="speakText()">Synthesize</button>
      <p id="result">Enter text above then click Synthesize</p>
    </div>
    <audio id="audioPlayback" controls>
      <source id="audioSource" type="audio/mp3" src="">
    </audio>
    <!-- (script elements go here) -->
 </body>
</html>
```

Save the HTML file, naming it `polly.html`. After you have created the user interface for the application, you're ready to add the browser script code that runs the application.

## Step 4: Write the Browser Script
<a name="getting-started-browser-write-sample"></a>

The first thing to do when creating the browser script is to include the SDK for JavaScript by adding a `<script>` element after the `<audio>` element in the page. To find the current SDK\_VERSION\_NUMBER, see the API Reference for the SDK for JavaScript at [AWS SDK for JavaScript API Reference Guide.](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/)

```
<script src="https://sdk.amazonaws.com/js/aws-sdk-{{SDK_VERSION_NUMBER}}.min.js"></script>
```

Then add a new `<script type="text/javascript">` element after the SDK entry. You'll add the browser script to this element. Set the AWS Region and credentials for the SDK. Next, create a function named `speakText()` that will be invoked as an event handler by the button.

To synthesize speech with Amazon Polly, you must provide a variety of parameters including the sound format of the output, the sampling rate, the ID of the voice to use, and the text to play back. When you initially create the parameters, set the `Text:` parameter to an empty string; the `Text:` parameter will be set to the value you retrieve from the `<input>` element in the webpage. Replace {{IDENTITY\_POOL\_ID}} and {{REGION}} in the following code with values noted in [Step 1: Create an Amazon Cognito Identity Pool](#getting-started-browser-create-identity-pool).

```
    <script type="text/javascript">

        // Initialize the Amazon Cognito credentials provider
        AWS.config.region = 'REGION';
        AWS.config.credentials = new AWS.CognitoIdentityCredentials({IdentityPoolId: 'IDENTITY_POOL_ID'});

        // Function invoked by button click
        function speakText() {
            // Create the JSON parameters for getSynthesizeSpeechUrl
            var speechParams = {
                OutputFormat: "mp3",
                SampleRate: "16000",
                Text: "",
                TextType: "text",
                VoiceId: "Matthew"
            };
            speechParams.Text = document.getElementById("textEntry").value;
```

Amazon Polly returns synthesized speech as an audio stream. The easiest way to play that audio in a browser is to have Amazon Polly make the audio available at a presigned URL you can then set as the `src` attribute of the `<audio>` element in the webpage.

Create a new `AWS.Polly` service object. Then create the `AWS.Polly.Presigner` object you'll use to create the presigned URL from which the synthesized speech audio can be retrieved. You must pass the speech parameters that you defined as well as the `AWS.Polly` service object that you created to the `AWS.Polly.Presigner` constructor.

After you create the presigner object, call the `getSynthesizeSpeechUrl` method of that object, passing the speech parameters. If successful, this method returns the URL of the synthesized speech, which you then assign to the `<audio>` element for playback.

```
            // Create the Polly service object and presigner object
            var polly = new AWS.Polly({apiVersion: '2016-06-10'});
            var signer = new AWS.Polly.Presigner(speechParams, polly)

            // Create presigned URL of synthesized speech file
            signer.getSynthesizeSpeechUrl(speechParams, function(error, url) {
            if (error) {
                document.getElementById('result').innerHTML = error;
            } else {
                document.getElementById('audioSource').src = url;
                document.getElementById('audioPlayback').load();
                document.getElementById('result').innerHTML = "Speech ready to play.";
            }
          });
        }
    </script>
```

## Step 5: Run the Sample
<a name="getting-started-browser-run-sample"></a>

To run the sample app, load `polly.html` into a web browser. This is what the browser presentation should resemble.

![Web application browser interface](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/images/browsergetstarted.png)

Enter a phrase you want turned to speech in the input box, then choose **Synthesize**. When the audio is ready to play, a message appears. Use the audio player controls to hear the synthesized speech.

## Full Sample
<a name="getting-started-browser-full-sample"></a>

Here is the full HTML page with the browser script. It's also available [here on GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javascript/example_code//browserstart/polly.html).

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>AWS SDK for JavaScript - Browser Getting Started Application</title>
  </head>

  <body>
    <div id="textToSynth">
      <input autofocus size="23" type="text" id="textEntry" value="It's very good to meet you."/>
      <button class="btn default" onClick="speakText()">Synthesize</button>
      <p id="result">Enter text above then click Synthesize</p>
    </div>
    <audio id="audioPlayback" controls>
      <source id="audioSource" type="audio/mp3" src="">
    </audio>
    <script src="https://sdk.amazonaws.com/js/aws-sdk-2.410.0.min.js"></script>
    <script type="text/javascript">

        // Initialize the Amazon Cognito credentials provider
        AWS.config.region = 'REGION';
        AWS.config.credentials = new AWS.CognitoIdentityCredentials({IdentityPoolId: 'IDENTITY_POOL_ID'});

        // Function invoked by button click
        function speakText() {
            // Create the JSON parameters for getSynthesizeSpeechUrl
            var speechParams = {
                OutputFormat: "mp3",
                SampleRate: "16000",
                Text: "",
                TextType: "text",
                VoiceId: "Matthew"
            };
            speechParams.Text = document.getElementById("textEntry").value;

            // Create the Polly service object and presigner object
            var polly = new AWS.Polly({apiVersion: '2016-06-10'});
            var signer = new AWS.Polly.Presigner(speechParams, polly)

            // Create presigned URL of synthesized speech file
            signer.getSynthesizeSpeechUrl(speechParams, function(error, url) {
            if (error) {
                document.getElementById('result').innerHTML = error;
            } else {
                document.getElementById('audioSource').src = url;
                document.getElementById('audioPlayback').load();
                document.getElementById('result').innerHTML = "Speech ready to play.";
            }
          });
        }
    </script>
  </body>
</html>
```

## Possible Enhancements
<a name="getting-started-browser-variations"></a>

Here are variations on this application you can use to further explore using the SDK for JavaScript in a browser script.
+ Experiment with other sound output formats.
+ Add the option to select any of the various voices provided by Amazon Polly.
+ Integrate an identity provider like Facebook or Amazon to use with the authenticated IAM role.
