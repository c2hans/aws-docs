---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/import-export-models.html
---

# Import and export models
<a name="import-export-models"></a>

## Import a model
<a name="import-a-model"></a>

![Import a model](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_import_model.png)

You can import a model that you’ve previously exported from either:

1. Your current DeepRacer on AWS deployment

1. Another DeepRacer on AWS deployment

1. The original AWS DeepRacer service

**Note**
Models that were exported from the AWS DeepRacer service a long time ago may not be compatible with DeepRacer on AWS as they were produced with an older version of the simulation application.

To do this, from the home page, click the **Your models** tab in the left sidebar, and click the **Import model** button towards the upper-right.

On the **Import model** screen, start by clicking **Upload folder**. This will open a file explorer where you can browse for an exported model on your local computer. Find the exported model folder that you would like to upload and double-click into it. You can then click **Upload** in the bottom-right of the explorer.

**Note**
If your exported model is in an archived or zipped format, you will need to extract it first before uploading.

After you have selected the folder to be uploaded, provide a name for your model and an optional description. When you are ready to proceed, click the **Import** button. You will be able to see the progress of all files being uploaded. Once all files are uploaded, you will be redirected to the model detail view where the status will show as **Importing**.

The model status will then resolve to **Ready** after the import process is completed.

## Export a virtual model
<a name="export-a-virtual-model"></a>

**Note**
Virtual models are exported in .tar.gz format. If you are using Windows, you will need to install 7-Zip or another program that is capable of extracting this type of file.

You can export a virtual model from DeepRacer on AWS to use on another deployment of DeepRacer on AWS, or simply keep as a backup. To do this, from the home page, click the **Your models** tab in the left sidebar, and click the model that you would like to export. On the model detail view, click **Actions** > **Download virtual model**. This will begin preparing the model for download. Once it is ready, your browser will begin downloading it into its normal downloads folder.

## Export a physical car model
<a name="export-a-physical-car-model"></a>

**Note**
Physical models are exported in .tar.gz format. If you are using Windows, you will need to install 7-Zip or another program that is capable of extracting this type of file.

You can export a physical car model from DeepRacer on AWS to use on a DeepRacer-compatible physical car. To do this, from the home page, click the **Your models** tab in the left sidebar, and click the model that you would like to export. On the model detail view, click **Actions** > **Download physical car model**. This will begin preparing the model for download. Once it is ready, your browser will begin downloading it into its normal downloads folder.

See [Operate your vehicle](https://docs.aws.amazon.com/deepracer/latest/developerguide/operate-deepracer-vehicle.html) for more information on how to upload the model to a physical car.

**Tip**
Admins and race facilitators can download physical car models for any user from the **Model management** page. See [Model management](admin-functions.md#model-management).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
