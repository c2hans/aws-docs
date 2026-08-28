---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-editing-add-models.html
---

# Add models to your scenes
<a name="scenes-editing-add-models"></a>

To add models to your scene, use the following procedure.

**Note**
To add models in your scene, you must first upload the models to the AWS IoT TwinMaker Resource Library. For more information, see [Upload resources to the AWS IoT TwinMaker Resource Library](scenes-using-resource-library.md).

1. On the scene composer page, choose the plus (**\+**) sign, and then choose **Add 3D model**.

1. On the **Add resource from resource library** window, choose the **CookieFactorMixer.glb** file, and then choose **Add**. Scene composer opens.

1. **Optional**: Choose the plus (**\+**) sign, and then choose **Add light**.

1. Choose each light option to see how they affect the scene.
![A scene canvas with the "Light type" and "Color" controls displayed for the selected cookie mixer.](http://docs.aws.amazon.com/iot-twinmaker/latest/guide/images/CookieMixerInScene.png)
**Note**
Scenes have default ambient lighting. To avoid frame rate loss, consider limiting the number of additional lights placed in your scene.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
