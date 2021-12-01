function getUrls(class_name) {
    imgs_normal = document.getElementsByClassName(class_name);
    str = "";
    for (let i = 0; i < imgs_normal.length; i++) {
        if (imgs_normal[i].src != undefined) {
            str += imgs_normal[i].src + '\n';
        }
    }
    return str;
}

normal = getUrls('shinydex-sprite-normal');
shini = getUrls('shinydex-sprite-shiny');