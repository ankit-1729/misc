import webbrowser

simultaneous_num_of_tabs = 100
curr_imageId = 40864

for i in range(curr_imageId, curr_imageId + simultaneous_num_of_tabs):
  webbrowser.open('https://pose-tool.pages.dev/imageId={imageId}'.format(imageId=i), new=2)
