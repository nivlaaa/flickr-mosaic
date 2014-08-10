# flickr mosaic

Flickr Mosaic is a projet to create large mosaics out of the most interesting pictures on Flickr. Given an input image, Flickr Mosaic will generate a new picture cobbled together from many different pictures pulled from Flickr.

# how it works

Interesting pictures are gathered from Flickr over time via the Flickr api. This means that the images comprising the mosaic will be editorially curated by Flickr for higher quality, aesthetically pleasing pictures. These pictures are cached (in this case on the local machine running the script) so that they can be processed quickly. Pictures are sorted into buckets (folders) based on their average RGB value.

