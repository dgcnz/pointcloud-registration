import open3d as o3d


def load_rgbd(file_prefix: str):
    rgb = o3d.io.read_image(f"{file_prefix}_rgb.jpg")
    print("hi")
    depth = o3d.io.read_image(f"{file_prefix}_depth.png")
    print("hi")
    print(rgb, depth)
    return o3d.geometry.RGBDImage.create_from_color_and_depth(rgb, depth)


def intrinsics(file_prefix: str):
    if file_prefix == "camera_01":
        return o3d.camera.PinholeCameraIntrinsic(640, 400, 478.21887,
                                                 478.21887, 310.83194,
                                                 192.39627)
    else:
        return o3d.camera.PinholeCameraIntrinsic(640, 400, 478.25311,
                                                 478.25311, 314.01566,
                                                 192.86667)


camera_01_rgbd = load_rgbd("camera_01")
print("hi")
camera_02_rgbd = load_rgbd("camera_02")
camera_01_intrinsics = intrinsics("camera_01")
camera_02_intrinsics = intrinsics("camera_02")

camera_01_pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    camera_01_rgbd, camera_01_intrinsics)

camera_02_pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
    camera_02_rgbd, camera_02_intrinsics)

o3d.visualization.draw_geometries([camera_01_pcd])
