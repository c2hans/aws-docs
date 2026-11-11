---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/manage-your-models.html
---

# Manage your models
<a name="manage-your-models"></a>

## Clone a model
<a name="clone-a-model"></a>

You can clone any model that you’ve created or imported, provided it is **not in an error state**, or **not currently being trained or evaluated**.

**Note**
You cannot clone a physical model. Physical models are for physical car deployment only.

To do this, from the home page, click the **Your models** tab in the left sidebar, and select the model that you would like to clone. With the model selected, click **Actions** > **Clone**. This will open the same wizard that is used for creating a model, but with the attributes of the model you selected populated in the wizard fields.

In the **Model checkpoint** section of the wizard, choose which checkpoint of the original model the clone will start training from: **Best** (default), the checkpoint with the highest average completion during training, or **Last**, the most recently evaluated checkpoint. The checkpoint you choose is shown in the details of the cloned model.

If you would like to keep the exact same configuration as the original model, simply click through the wizard and click **Create** at the end to create the model. Otherwise, you can make adjustments to any aspect of the original model’s configuration before creating it.

## Delete a model
<a name="delete-a-model"></a>

You can delete any model that you’ve created or imported. To do this, from the home page, click the **Your models** tab in the left sidebar, and select the model that you would like to delete. With the model selected, click **Actions** > **Delete**. You will be presented with a confirmation dialog. If you would like to proceed, click **Delete**. This action is permanent and cannot be undone.
