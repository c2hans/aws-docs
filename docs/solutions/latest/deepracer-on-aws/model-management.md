---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/model-management.html
---

# Model management
<a name="model-management"></a>

**Note**
This section is available to both admins and race facilitators. In the console, these pages live under the **Model Management** group in the navigation pane.

Admins and race facilitators can optimize models for physical cars and push optimized models to cars. They can also download physical car models and view upload status. Perform these tasks from the **Model Management** group in the navigation pane. For more information about who can perform each task, see [Permissions matrix](types-of-users.md#permissions-matrix). Racers import their own physical models from the **Your models** page. For more information, see [Import and export models](import-export-models.md).

## Find and optimize a model
<a name="find-and-optimize-a-model"></a>

You optimize a virtual model for a physical car before you push it to that car. Optimization is non-blocking: a failed optimization never blocks virtual racing.

The following image shows the **Models** page, where you filter models by username and optimize a selected model for a car.

![Models page listing models with optimization status and optimize action](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/model-management/admin-models-list.png)

1. In the navigation pane, under **Model Management**, choose **Models**.

1. Filter the list by **Username** to find a racer’s model.

1. Select one model that has a **READY** status.

1. Choose **Optimize for car**.

On the **Models** page, the status shows as **Not optimized**, then **In progress**, then **Optimized** when it completes, or **Failed** if it does not. A failed optimization does not affect virtual racing, and you can run the optimization again.

## Push a model to a car
<a name="push-a-model-to-a-car"></a>

You push one or more optimized models to a physical car over a wireless connection. The car must first be activated through Device Management.

The following image shows the upload-to-car progress view, with per-model status and a progress bar.

![Upload to car progress view with per-model status and progress bar](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/model-management/car-upload-progress.png)

1. In the navigation pane, under **Model Management**, choose **Models**.

1. Select one or more optimized models. To push several models at once, select multiple models.

1. Choose **Upload model to car**.

1. For **Event**, choose an event.

1. Select an online car.

1. (Optional) To remove existing models from the car before the upload, select **Clear car models first?**.

1. Choose **Upload model to car** to start the upload.

**Note**
The solution automatically delivers the correct model format for your car. It supports three physical car types: an unmodified AWS DeepRacer car, an AWS DeepRacer running a custom operating system, and a Raspberry Pi-based custom car.

## Download a physical car model
<a name="download-a-physical-car-model"></a>

You can download any user’s model in physical car format from the **Models** page.

1. In the navigation pane, under **Model Management**, choose **Models**.

1. Filter the list by **Username** to find a racer’s model.

1. Choose **Download** next to the model to download it in physical car format.

**Note**
Physical models are exported in .tar.gz format. If you are using Windows, you will need to install 7-Zip or another program that is capable of extracting this type of file.

## View upload status
<a name="view-upload-status"></a>

You can review the history of your uploads to cars on the **Upload Status** page, which has the page header **Uploads to car status**.

The following image shows the **Upload Status** page, listing past uploads to cars and their status.

![Upload Status page listing past uploads to cars and their status](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/model-management/upload-status.png)

1. In the navigation pane, under **Model Management**, choose **Upload Status**.

1. Review the status of each upload to a car.
