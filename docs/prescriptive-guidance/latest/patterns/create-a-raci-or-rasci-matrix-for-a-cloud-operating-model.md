---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-raci-or-rasci-matrix-for-a-cloud-operating-model.html
---

# Create a RACI or RASCI matrix for a cloud operating model
<a name="create-a-raci-or-rasci-matrix-for-a-cloud-operating-model"></a>

*Teddy Germade, Jerome Descreux, Florian Leroux, and Josselin LE MINEUR, Amazon Web Services*

## Summary
<a name="create-a-raci-or-rasci-matrix-for-a-cloud-operating-model-summary"></a>

The Cloud Center of Excellence (CCoE) or CEE (Cloud Enablement Engine) is an empowered and accountable team that is focused on operational readiness for the cloud. Their key focus is to transform the information IT organization from an on-premises operating model to a cloud operating model. The CCoE should be a cross-functional team that includes representation from infrastructure, applications, operations, and security.

One of the key components of a cloud operating model is a *RACI matrix* or *RASCI matrix*. This is used to define the roles and responsibilities for all parties involved in migration activities and cloud operations. The matrix name is derived from the responsibility types defined in the matrix: responsible (R), accountable (A), support (S), consulted (C), and informed (I). The support type is optional. If you include it, it’s called a *RASCI matrix*, and if you exclude it, it’s called a *RACI matrix*.

By starting with the attached template, your CCoE team can create a RACI or RASCI matrix for your organization. The template contains teams, roles, and tasks that are common in cloud operating models. The foundation of this matrix is the tasks related to operations integration and CCoE capabilities. However, you can customize this template to meet the needs of your organization’s structure and use case.

There are no limits to the implementation of a RACI matrix. This approach works for large organizations, start-ups, and everything in between. For small organizations, the same resource can fill several roles.

## Epics
<a name="create-a-raci-or-rasci-matrix-for-a-cloud-operating-model-epics"></a>

### Create the matrix
<a name="create-the-matrix"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify key stakeholders. | Identify key service and team managers that are linked to the strategic objectives of your cloud operating model. | Project manager |
| Customize the matrix template. | Download the template in the [Attachments](#attachments-b3df3d2c-c596-4736-bbaa-8edbcf335352) section, and then update the RACI or RASCI matrix as follows:+ On the **Cloud Teams** worksheet, update the CCoE stream names, team names, and team descriptions as needed for your organization.<br />+ On the **Cloud Roles** worksheet, update the roles, team names, and role descriptions as needed for your organization.<br />+ On the **RASCI** worksheet, update the following as needed for your organization:In row 1 and column A, update the CCoE streams.In row 2, update the team names.In row 3, update the role names.In columns D and E, update the general fields and activities that you want to include in your RASCI chart. | Project manager |
| Plan meetings. | 1. Communicate the RASCI objectives to all stakeholders.<br />2. Plan one or more meetings so that an empowered representative from each team can attend. | Project manager |
| Complete the matrix. | In the meeting with all stakeholders, do the following:1. Confirm that a representative from each team is present. Team participation is mandatory so that you can accurately assign responsibility types for each task.<br />2. Review the what a RASCI matrix is and the objectives with the participants.<br />3. Review the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) with the participants so that they understand the scope of their organization’s responsibilities for security in the cloud.<br />4. On the **RASCI** worksheet, for each task or activity, complete columns F through AN to assign the following responsibility types:**Responsible (R)** – This role is responsible for performing the work to complete the task.**Accountable (A)** – This role is held accountable for making sure the task is completed. This role is also responsible for ensuring the prerequisites are met and delegating the task to those who are responsible.**Support (S)** – This role helps those who are responsible complete the task. This responsibility type is optional, and you can choose to exclude it in order to create a more traditional RACI matrix.**Consulted (C)** – This role should be consulted for opinions or expertise on the task. Depending on the task, this responsibility type might not be required.**Informed (I)** – This role should be kept up to date on the progress of the task and notified when the task is completed.**Blank **– This role is not involved in the activity or task. | Project manager |
| Share the RASCI matrix. | When the RACI or RASCI matrix is complete, have it approved by leadership. Save it in a shared repository or central location where all stakeholders can access it. We recommend that you use standard document control processes to record and approve revisions to the matrix. | Project manager |

## Related resources
<a name="create-a-raci-or-rasci-matrix-for-a-cloud-operating-model-resources"></a>
+ [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/)

## Attachments
<a name="attachments-b3df3d2c-c596-4736-bbaa-8edbcf335352"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/b3df3d2c-c596-4736-bbaa-8edbcf335352/attachments/attachment.zip)
