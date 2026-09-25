---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/import-export-models.html
---

# Import and export models
<a name="import-export-models"></a>

## Import a model
<a name="import-a-model"></a>

![Import a model](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_import_model.png)

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

## Import a physical model
<a name="import-a-physical-model"></a>

You can import a pre-trained physical model directly on the **Your models** page. A physical model is deployment-only. You can push it to a physical car, but you can’t clone it or submit it to a community race.

The following image shows the **Import physical model** page, where you choose a model archive and enter a name.

![Import physical model page with file picker and model name field](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/model-management/import-physical-model.png)

1. From the home page, choose the **Your models** tab in the left sidebar.

1. Choose **Import model**, then choose **Import physical model**.

1. Choose the model archive to upload. The file must be in `.tar.gz` format and can be a maximum of 500 MB.

1. Enter a model name. The name can be up to 64 characters and can contain only letters, numbers, and hyphens.

1. Choose **Import** to start the import.

The number of physical models you can import is limited by your model count quota. Each uploaded file is automatically scanned for malware before it becomes available. After the import completes, the result is a physical model that you can deploy to a car. For more information about optimizing and pushing models to cars, see [Model management](model-management.md).

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
Admins and race facilitators can download physical car models for any user from the **Model management** page. See [Model management](model-management.md).
