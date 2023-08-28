from graph_onedrive import OneDriveManager

# Use a context manager to manage the session
with OneDriveManager(config_path="config.json", config_key="onedrive") as my_drive:

    my_drive.get_usage(verbose=True)

    items = my_drive.list_directory(folder_id="01CVXDX5BOYX7TAEL6PBFIRA7D37DECXLP", verbose=False)

    if len(items) > 7:
        for i in range(0,7):
            print("删除文件："+items[i]['name'])
            confirmation = my_drive.delete_item(items[i]['id'], pre_confirm=True)
            print(confirmation)
    else:
        print("当前文件数量未达到设定值")
