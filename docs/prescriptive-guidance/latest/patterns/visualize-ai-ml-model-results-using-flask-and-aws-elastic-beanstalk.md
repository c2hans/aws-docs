---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk.html
---

# Visualize AI/ML model results using Flask and AWS Elastic Beanstalk
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk"></a>

*Chris Caudill and Durga Sury, Amazon Web Services*

## Summary
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-summary"></a>

Visualizing output from artificial intelligence and machine learning (AI/ML) services often requires complex API calls that must be customized by your developers and engineers. This can be a drawback if your analysts want to quickly explore a new dataset.

You can enhance the accessibility of your services and provide a more interactive form of data analysis by using a web-based user interface (UI) that enables users to upload their own data and visualize the model results in a dashboard.

This pattern uses [Flask](https://flask.palletsprojects.com/en/stable/) and [Plotly](https://plotly.com/) to integrate Amazon Comprehend with a custom web application and visualize sentiments and entities from user-provided data. The pattern also provides the steps to deploy an application by using AWS Elastic Beanstalk. You can adapt the application by using [AWS AI services](https://aws.amazon.com/machine-learning/ai-services/) or with a custom trained model hosted on an endpoint (for example, an [Amazon SageMaker endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)).

## Prerequisites and limitations
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI), installed and configured on your local machine. For more information about this, see [Configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the AWS CLI documentation. You can also use an AWS Cloud9 integrated development environment (IDE); for more information about this, see [Python tutorial for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/sample-python.html) and [Previewing running applications in the AWS Cloud9 IDE](https://docs.aws.amazon.com/cloud9/latest/user-guide/app-preview.html) in the AWS Cloud9 documentation.

  **Notice**: AWS Cloud9 is no longer available to new customers. Existing customers of AWS Cloud9 can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/)
+ An understanding of Flask’s web application framework. For more information about Flask, see the [Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/) in the Flask documentation.
+ Python version 3.6 or later, installed and configured. You can install Python by following the instructions from [Setting up your Python development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-development-environment.html) in the AWS Elastic Beanstalk documentation.
+ Elastic Beanstalk Command Line Interface (EB CLI), installed and configured. For more information about this, see [Install the EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) and [Configure the EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html) from the Elastic Beanstalk documentation.

**Limitations**
+ This pattern’s Flask application is designed to work with .csv files that use a single text column and are restricted to 200 rows. The application code can be adapted to handle other file types and data volumes.
+ The application doesn’t consider data retention and continues to aggregate uploaded user files until they are manually deleted. You can integrate the application with Amazon Simple Storage Service (Amazon S3) for persistent object storage or use a database such as Amazon DynamoDB for serverless key-value storage.
+ The application only considers documents in the English language. However, you can use Amazon Comprehend to detect a document’s primary language. For more information about the supported languages for each action, see [API reference](https://docs.aws.amazon.com/comprehend/latest/dg/API_Reference.html) in the Amazon Comprehend documentation.

## Architecture
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-architecture"></a>

**Flask application architecture**

Flask is a lightweight framework for developing web applications in Python. It is designed to combine Python’s powerful data processing with a rich web UI. The pattern’s Flask application shows you how to build a web application that enables users to upload data, sends the data to Amazon Comprehend for inference, and then visualizes the results.   The application has the following structure:
+ `static` – Contains all the static files that support the web UI (for example, JavaScript, CSS, and images)
+ `templates` – Contains all of the application's HTML pages
+ `userData` – Stores uploaded user data
+ `application.py` – The Flask application file
+ `comprehend_helper.py` – Functions to make API calls to Amazon Comprehend
+ `config.py` – The application configuration file
+ `requirements.txt` – The Python dependencies required by the application

The `application.py` script contains the web application's core functionality, which consists of four Flask routes. The following diagram shows these Flask routes.

![The four Flask routes that make up the web application's core functionality.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/03d80cf1-ec97-43f7-adb5-2746a9ec70e6/images/9ca6bad1-26e2-4262-98d0-d54c172336bf.png)

+ `/` is the application's root and directs users to the `upload.html` page (stored in the `templates` directory).
+ `/saveFile` is a route that is invoked after a user uploads a file. This route receives a `POST` request via an HTML form, which contains the file uploaded by the user. The file is saved in the `userData` directory and the route redirects users to the `/dashboard` route.
+ `/dashboard` sends users to the `dashboard.html` page. Within this page's HTML, it runs the JavaScript code in `static/js/core.js` that reads data from the `/data` route and then builds visualizations for the page.
+ `/data` is a JSON API that presents the data to be visualized in the dashboard. This route reads the user-provided data and uses the functions in `comprehend_helper.py` to send the user data to Amazon Comprehend for sentiment analysis and named entity recognition (NER). The Amazon Comprehend response is formatted and returned as a JSON object.

**Deployment architecture**

![Architecture diagram for using Flask and Elastic Beanstalk to visualize AI/ML model results.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/03d80cf1-ec97-43f7-adb5-2746a9ec70e6/images/d691bfd2-e2ec-4830-8bff-ffa1e3a95c4a.png)

[Design considerations](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.concepts.design.html)

 For more information about design considerations for applications deployed using Elastic Beanstalk on the AWS Cloud, see in the AWS Elastic Beanstalk documentation.

**Technology stack**
+ Amazon Comprehend
+ Elastic Beanstalk
+ Flask

**Automation and scale**

Elastic Beanstalk deployments are automatically set up with load balancers and auto scaling groups. For more configuration options, see [Configuring Elastic Beanstalk environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customize-containers.html) in the Elastic Beanstalk documentation.

## Tools
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is a unified tool that provides a consistent interface for interacting with all parts of AWS.
+ [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-general.html) uses natural language processing (NLP) to extract insights about the content of documents without requiring special preprocessing.
+ [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) helps you quickly deploy and manage applications in the AWS Cloud without having to learn about the infrastructure that runs those applications.
+ [Elastic Beanstalk CLI (EB CLI)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html) is a command line interface for AWS Elastic Beanstalk that provides interactive commands to simplify creating, updating, and monitoring environments from a local repository.
+ The [Flask](https://flask.palletsprojects.com/en/stable/) framework performs data processing and API calls using Python and offers interactive web visualization with Plotly.

**Code repository**

The code for this pattern is available in the GitHub [Visualize AI/ML model results using Flask and AWS Elastic Beanstalk](https://github.com/aws-samples/aws-comprehend-elasticbeanstalk-for-flask) repository.

## Epics
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-epics"></a>

### Set up the Flask application
<a name="set-up-the-flask-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | Pull the application code from the GitHub [Visualize AI/ML model results using Flask and AWS Elastic Beanstalk](https://github.com/aws-samples/aws-comprehend-elasticbeanstalk-for-flask) repository by running the following command:<br />`git clone git@github.com:aws-samples/aws-comprehend-elasticbeanstalk-for-flask.git`Make sure that you configure your SSH keys with GitHub. | Developer |
| Install the Python modules. | After you clone the repository, a new local `aws-comprehend-elasticbeanstalk-for-flask` directory is created. In that directory, the `requirements.txt` file contains the Python modules and versions that run the application. Use the following commands to install the modules:<br />`cd aws-comprehend-elasticbeanstalk-for-flask`<br />`pip install -r requirements.txt` | Python developer |
| Test the application locally. | Start the Flask server by running the following command:<br />`python application.py`<br />This returns information about the running server. You should be able to access the application by opening a browser and visiting http://localhost:5000If you're running the application in an AWS Cloud9 IDE, you need to replace the `application.run()` command in the `application.py` file with the following line:<br />`application.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))`<br />You must revert this change before deployment. | Python developer |

### Deploy the application to Elastic Beanstalk
<a name="deploy-the-application-to-aeb"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the Elastic Beanstalk application. | To launch your project as an Elastic Beanstalk application, run the following command from your application’s root directory:<br />`eb init -p python-3.6 comprehend_flask --region us-east-1` [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk.html)<br />Run the `eb init -i` command for more deployment configuration options. | Architect, Developer |
| Deploy the Elastic Beanstalk environment. | Run the following command from the application's root directory:<br />`eb create comprehend-flask-env``comprehend-flask-env` is the name of the Elastic Beanstalk environment and can be changed according to your requirements. The name can only contain letters, numbers, and dashes. | Architect, Developer |
| Authorize your deployment to use Amazon Comprehend. | Although your application might be successfully deployed, you should also provide your deployment with access to Amazon Comprehend. `ComprehendFullAccess` is an AWS managed policy that provides the deployed application with permissions to make API calls to Amazon Comprehend.<br />Attach the `ComprehendFullAccess` policy to `aws-elasticbeanstalk-ec2-role` (this role is automatically created for your deployment’s Amazon Elastic Compute Cloud (Amazon EC2) instances) by running the following command:<br />`aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/ComprehendFullAccess --role-name aws-elasticbeanstalk-ec2-role``aws-elasticbeanstalk-ec2-role` is created when your application deploys. You must complete the deployment process before you can attach the AWS Identity and Access Management (IAM) policy. | Developer, Security architect |
| Visit your deployed application. | After your application successfully deploys, you can visit it by running the `eb open` command.<br />You can also run the `eb status` command to receive details about your deployment. The deployment URL is listed under `CNAME`. | Architect, Developer |

### (Optional) Customize the application to your ML model
<a name="optional-customize-the-application-to-your-ml-model"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Authorize Elastic Beanstalk to access the new model. | Make sure that Elastic Beanstalk has the required access permissions for your new model endpoint. For example, if you use an Amazon SageMaker AI endpoint, your deployment needs to have permission to invoke the endpoint. <br />For more information about this, see [InvokeEndpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html) in the Amazon SageMaker AI documentation. | Developer, Security architect |
| Send the user data to a new model. | To change the underlying ML model in this application, you must change the following files:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk.html) | Data scientist |
| Update the dashboard visualizations. | Typically, incorporating a new ML model means that visualizations must be updated to reflect the new results. These changes are made in the following files:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk.html) | Web developer |

### (Optional) Deploy the updated application
<a name="optional-deploy-the-updated-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update your application's requirements file. | Before sending changes to Elastic Beanstalk, update the `requirements.txt` file to reflect any new Python modules by running the following command in your application's root directory:<br />`pip freeze > requirements.txt` | Python developer |
| Redeploy the Elastic Beanstalk environment. | To ensure that your application changes are reflected in your Elastic Beanstalk deployment, navigate to your application's root directory and run the following command:<br />`eb deploy`<br />This sends the most recent version of the application's code to your existing Elastic Beanstalk deployment. | Systems administrator, Architect |

## Troubleshooting
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `Unable to assume role "arn:aws:iam::xxxxxxxxxx:role/aws-elasticbeanstalk-ec2-role". Verify that the role exists and is configured correctly.` | If this error occurs when you run `eb create`, create a sample application on the Elastic Beanstalk console to create the default instance profile. For more information about this, see [Creating an Elastic Beanstalk environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.environments.html) in the AWS Elastic Beanstalk documentation. |
| `Your WSGIPath refers to a file that does not exist.` | This error occurs in deployment logs because Elastic Beanstalk expects the Flask code to be named `application.py`. If you chose a different name, run `eb config` and edit the WSGIPath as shown in the following code sample:<pre>aws:elasticbeanstalk:container:python:<br />     NumProcesses: '1'<br />     NumThreads: '15'<br />     StaticFiles: /static/=static/<br />     WSGIPath: application.py</pre><br />Make sure that you replace `application.py` with your file name.<br />You can also leverage Gunicorn and a Procfile. For more information about this approach, see [Configuring the WSGI server with a Procfile](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-configuration-procfile.html) in the AWS Elastic Beanstalk documentation. |
| `Target WSGI script '/opt/python/current/app/application.py' does not contain WSGI application 'application'.` | Elastic Beanstalk expects the variable that represents your Flask application to be named `application`. Make sure that the `application.py` file uses `application` as the variable name:<pre>application = Flask(__name__)</pre> |
| `The EB CLI cannot find your SSH key file for keyname` | Use the EB CLI to specify which key pair to use or to create a key pair for your deployment’s Amazon EC2 instances. To resolve the error, run `eb init -i` and one of the options will ask:<pre>Do you want to set up SSH for your instances?</pre><br />Respond with `Y` to either create a key pair or specify an existing key pair. |
| I’ve updated my code and redeployed, but my deployment is not reflecting my changes. | If you’re using a Git repository with your deployment, make sure that you add and commit your changes before redeploying. |
| You are previewing the Flask application from an AWS Cloud9 IDE and run into errors. | For more information about this, see [Previewing running applications in the AWS Cloud9 IDE](https://docs.aws.amazon.com/cloud9/latest/user-guide/app-preview.html) in the AWS Cloud9 documentation. |

## Related resources
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-resources"></a>
+ [Call an Amazon SageMaker AI model endpoint using Amazon API Gateway and AWS Lambda](https://aws.amazon.com/blogs/machine-learning/call-an-amazon-sagemaker-model-endpoint-using-amazon-api-gateway-and-aws-lambda/)
+ [Deploying a Flask application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
+ [EB CLI command reference](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html)
+ [Setting up your Python development environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/python-development-environment.html)

## Additional information
<a name="visualize-ai-ml-model-results-using-flask-and-aws-elastic-beanstalk-additional"></a>

*Natural language processing using Amazon Comprehend*

By choosing to use Amazon Comprehend, you can detect custom entities in individual text documents by running real-time analysis or asynchronous batch jobs. Amazon Comprehend also enables you to train custom entity recognition and text classification models that can be used in real time by creating an endpoint.

This pattern uses asynchronous batch jobs to detect sentiments and entities from an input file that contains multiple documents. The sample application provided by this pattern is designed for users to upload a .csv file containing a single column with one text document per row. The `comprehend_helper.py` file in the GitHub [Visualize AI/ML model results using Flask and AWS Elastic Beanstalk](https://github.com/aws-samples/aws-comprehend-elasticbeanstalk-for-flask) repository reads the input file and sends the input to Amazon Comprehend for processing.

*BatchDetectEntities*

Amazon Comprehend inspects the text of a batch of documents for named entities and returns the detected entity, location, [type of entity](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html), and a score that indicates the Amazon Comprehend level of confidence. A maximum of 25 documents can be sent in one API call, with each document smaller than 5,000 bytes in size. You can filter the results to show only certain entities based on the use case. For example, you could skip the `‘quantity’` entity type and set a threshold score for the detected entity (for example, 0.75). We recommend that you explore the results for your specific use case before choosing a threshold value. For more information about this, see [BatchDetectEntities](https://docs.aws.amazon.com/comprehend/latest/dg/API_BatchDetectEntities.html) in the Amazon Comprehend documentation.

*BatchDetectSentiment*

Amazon Comprehend inspects a batch of incoming documents and returns the prevailing sentiment for each document (`POSITIVE`, `NEUTRAL`, `MIXED`, or `NEGATIVE`). A maximum of 25 documents can be sent in one API call, with each document smaller than 5,000 bytes in size. Analyzing the sentiment is straightforward and you choose the sentiment with the highest score to be displayed in the final results. For more information about this, see [BatchDetectSentiment](https://docs.aws.amazon.com/comprehend/latest/dg/API_BatchDetectSentiment.html) in the Amazon Comprehend documentation.

*Flask configuration handling*

Flask servers use a series of [configuration variables](https://flask.palletsprojects.com/en/stable/config/) to control how the server runs. These variables can contain debug output, session tokens, or other application settings. You can also define custom variables that can be accessed while the application is running. There are multiple approaches for setting configuration variables.

In this pattern, the configuration is defined in `config.py` and inherited within `application.py`.
+ `config.py` contains the configuration variables that are set up on the application's startup. In this application, a `DEBUG` variable is defined to tell the application to run the server in [debug mode](https://flask.palletsprojects.com/en/stable/config/#DEBUG).
**Note**
Debug mode should not be used when running an application in a production environment. `UPLOAD_FOLDER` is a custom variable that is defined to be referenced later in the application and inform it where uploaded user data should be stored.
+ `application.py` initiates the Flask application and inherits the configuration settings defined in `config.py`. This is performed by the following code:

```
application = Flask(__name__)
application.config.from_pyfile('config.py')
```
