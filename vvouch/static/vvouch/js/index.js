$(document).ready(function () {
    $('.permission-select').select2({
        dropdownParent: $("#exampleModal")
    });

    $('.subCategory-permission-select').select2({
        dropdownParent: $("#subModal")
    });

    $('.category-select').select2({
        dropdownParent: $("#subModal")
    });

    $('.archivo-category-select').select2({
        dropdownParent: $("#archivoModal")
    });

    $('.archivo-subcategory-select').select2({
        dropdownParent: $("#archivoModal")
    });

    $('.edit-permission-select').select2({
        dropdownParent: $("#editModal")
    });

    $('.edit-category-select').select2({
        dropdownParent: $("#editSubModal")
    });

    $('.edit-sub-permission-select').select2({
        dropdownParent: $("#editSubModal")
    })

    $('.category-select').change(function(e) {

            var postRoute = '/get-subcategory-permission'
            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "json",
                data: {
                    csrfmiddlewaretoken: $(".csrfToken").val(),
                    'category_title': $(".category-select").val(),
                },
            }).done(function (data) {
                $(".subCategory-permission-select").empty();
                for(var key in data['data']) {
                    let permissionData = data['data'][key]
                    $(".subCategory-permission-select").append('<option value="' + permissionData + '">' + permissionData + '</option>')        
                    
                    $(".subCategory-permission-select > option").each(function() {
                        $(this).prop("selected",true);
                    });
                }
            });      
    }); 

    $("#subCat_Edit").change(function(e) {

        var postRoute = '/get-subcategory-permission';

        $.ajax({
            type: "POST",
            url: postRoute,
            dataType: "json",
            data: {
                csrfmiddlewaretoken: $(".csrfToken").val(),
                'category_title': $("#subCat_Edit").val(),
            },
        }).done(function (data) {
            $(".edit-sub-permission-select").empty();
            for(var key in data['data']) {
                let permissionData = data['data'][key];
                $(".edit-sub-permission-select").append('<option value="' + permissionData + '">' + permissionData + '</option>');        
            }
        });

    });

    //     $.ajax({
    //         type: "POST",
    //         url: '/get_edit_subcategory_permission',
    //         dataType: "json",
    //         data: {
    //             csrfmiddlewaretoken: $(".csrfToken").val(),
    //             'category_title': $("#old-category-select").val(),
    //             'subcategories_title': $("#edit-subcategory-name").val()
    //         },
    //     }).done(function (data) {
    //         for(var key in data['data']) {
    //             let permissionData = data['data'][key]
            
    //             $(".edit-sub-permission-select > option").each(function () {
    //                 if ($(this).val() === permissionData) {
    //                     console.log("Worked!");
    //                     $(this).prop('selected',true)
    //                 }
    //             });

            
    //             $(".edit-sub-permission-select").trigger("change");
    //         }
    //     });

    // }); 

    $.ajax({
        type: "GET",
        url: "https://uoapp.es/wp-json/custom-api/v2/get_users_roles",
    }).done(function (data) {
        for (key in data) {
            $(".permission-select").append('<option value="' + key + '">' + key + '</option>')
            $(".edit-permission-select").append('<option value="' + key + '">' + key + '</option>')
        }
    }).error(function (data) {
        swal("Oops", "algo salió mal...!", "error");
    });

    $("body").undelegate(".create-category", "click").delegate(".create-category", "click", function () {
        var all_ok = false;
        if ($("#category-name").val() == "" || $("#category-name").val() == null) {
            swal("Oops", "Escriba el nombre de la categoría..!", "error");
        } else if ($(".permission-select").val() == "" || $(".permission-select").val() == null) {
            swal("Oops", "Seleccione los permisos..!", "error");
        } else {
            all_ok = true;
        }
        if (all_ok == true) {
            var __this = $(this);
            var postRoute = '/add-category';

            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "json",
                data: {
                    csrfmiddlewaretoken: $(".csrfToken").val(),
                    'category_title': $("#category-name").val(),
                    'permissions': JSON.stringify($(".permission-select").val()),
                },
            }).done(function (data) {
                if (data.success == 1) {
                    swal("Éxito!", "Categoría creada con éxito...!", "success")
                        .then((value) => {
                            location.reload();
                        });
                } else if (data.error == 2) {
                    swal("Oops", "La categoría ya existe..!", "error");
                } else {
                    swal("Oops", "algo salió mal. Category is not created...!", "error");
                }
            }).error(function (data) {
                swal("Oops", "algo salió mal...!", "error");
            });
        }
    });

    $("body").undelegate(".create-subcategory", "click").delegate(".create-subcategory", "click", function () {
        var all_ok = false;
        if ($("#subcategory-name").val() == "" || $("#category-name").val() == null) {
            swal("Oops", "Escriba el nombre de la subcategoría..!", "error");
        } else if ($(".category-select").val() == "" || $(".category-select").val() == null) {
            swal("Oops", "Seleccione una categoría..!", "error");
        } else if($('.subCategory-permission-select').val() == null) {
            swal("Oops", "Seleccione los permisos..!", "error");          
        } else {
            all_ok = true;
        }
        if (all_ok == true) {
            var __this = $(this);
            var postRoute = '/add-subcategory';
            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "json",
                data: {
                    csrfmiddlewaretoken: $(".csrfToken").val(),
                    'subcategory_title': $("#subcategory-name").val(),
                    'category': $(".category-select").val(),
                    'permissions': JSON.stringify($('.subCategory-permission-select').val())
                },
            }).done(function (data) {
                if (data.success == 1) {
                    swal("Éxito!", "Subcategoría creada con éxito...!", "success")
                        .then((value) => {
                            location.reload();
                        });
                } else if (data.error == 2) {
                    swal("Oops", "La categoría ya existe..!", "error");
                } else {
                    swal("Oops", "Hubo algún erorr. La subcategoría no se actualizó..!", "error");
                }
            }).error(function (data) {
                swal("Oops", "algo salió mal...!", "error");
            });
        }
    });


    function progress(e){

        if(e.lengthComputable){
            var max = e.total;
            var current = e.loaded;
    
            var percent = parseInt((current * 100)/max);
            $('#progressBar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
        }  
     }
     
    $("#archivo-form").on("submit", function (evt) {
        evt.preventDefault();
        var all_ok = false;
        if ($(".archivo-category-select").val() == "" || $(".archivo-category-select").val() == null) {
            swal("Oops", "Seleccione una categoría..!", "error");
        } else {
            all_ok = true;
        }

        if (all_ok == true) {
                if($("#cat-sub-files")[0].files.length > 0) {
                    var __this = $(this);
                    var postRoute = '/add-archivo';
                    var formData = new FormData(this)

                    var xhr = new XMLHttpRequest()
                    xhr.upload.addEventListener("progress", progress, false)
                    // xhr.onreadystatechange = function(e) {
                    //     if ( 4 == this.readyState ) {
                    //         console.log(['xhr upload complete', e]);
                    //     }
                    // };
                    
                    xhr.open("POST", postRoute)
                    xhr.setRequestHeader("Content-Type","multipart/form-data");
                    xhr.send(formData)

                   

                    $.ajax({
                        xhr: function(){
                            var myXhr = $.ajaxSettings.xhr();
                            if(myXhr.upload){
                                var xhr = new XMLHttpRequest()
                                xhr.upload.addEventListener("progress", progress, false)
                            }

                            return myXhr;
                        },
                        type: "POST",
                        url: postRoute,
                        // dataType: "multipart/form-data",
                        data: new FormData(this),
                        // async: false,
                        cache: false,
                        contentType: false,
                        processData: false,
                        beforeSend: function(xhr) {
                            console.log(xhr);
                            if(xhr.upload) {
                                console.log("Upload")
                            }
                        },
                        success: function (data) {
                            console.log(data);
                            $('.create-archivo').removeAttr('disabled').text('Crear')
                            if (data.success == 1) {
                                swal("Éxito!", "Imágenes subidas con éxito!", "success")
                                    .then((value) => {
                                        location.reload();
                                    });
                            } else if (data.error == 2) {
                                swal("Oops", "La categoría ya existe..!", "error");
                            } else {
                                swal("Oops", "algo salió mal...!", "error");
                            }
                        },
                        error: function (data) {
                            $('.create-archivo').removeAttr('disabled').text('Crear')
                            swal("Éxito!", "Imágenes subidas con éxito!", "success")
                                .then((value) => {
                                    location.reload();
                                });
                        }

                    });       
                } else {
                    swal("Oops","No hay archivos adjuntados","error")
                }
        }
    });

    $(".archivo-category-select").on("change", function () {
        $(".archivo-subcategory-select").each(function () {
            $(this).find("option").remove();
        });
        var all_ok = false;
        if ($(".archivo-category-select").val() == "" || $(".archivo-category-select").val() == null) {
            swal("Oops", "Seleccione una categoría..!", "error");
        } else {
            all_ok = true;
        }
        if (all_ok == true) {
            var __this = $(this);
            var postRoute = '/get-subcategory';
            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "json",
                data: {
                    csrfmiddlewaretoken: $(".csrfToken").val(),
                    'category_title': $(".archivo-category-select").val()
                },
            }).done(function (data) {
                var dataSet = data.data;
                $(".archivo-subcategory-select").append('<option value="">Seleccionar subcategoría</option>');
                if (data.success == 1) {
                    for (var i = 0; i < dataSet.length; i++) {
                        var result = dataSet[i];
                        $(".archivo-subcategory-select").append('<option value="' + result.subcategory_title + '">' + result.subcategory_title + '</option>');
                    }
                } else {
                    swal("Oops", "algo salió mal/Subcategory did not exists...", "error");
                }
            }).error(function (data) {
                swal("Oops", "algo salió mal...!", "error");
            });
        }
    });

    // edit
    $("body").undelegate(".editCategoryButton", "click").delegate(".editCategoryButton", "click", function () {
        $(".edit-permission-select > option").each(function () {
            $(this).removeAttr("selected");
        });
        $(".edit-permission-select").trigger("change");
        $("#edit-category-name").val($.trim($(this).parent().parent().find(".bold-text").text()));
        $("#old-category-name").val($.trim($(this).parent().parent().find(".bold-text").text()));
        data = $(this).attr("data-set");
        if (data) {
            dataJson = data.replace('[', '');
            dataJson = dataJson.replace(']', '');
        }
        if (dataJson) {
            dataJson = dataJson.split(",");
            for (var i = 0; i < dataJson.length; i++) {
                var newData = dataJson[i];
                newData = newData.replace("'", '');
                newData = newData.replace("'", '');
                $(".edit-permission-select > option").each(function () {
                    if ($(this).val() == $.trim(newData)) {
                        $(this).prop("selected", "selected");
                    }
                });
                $(".edit-permission-select").trigger("change");
            }
        }
    });

    $("body").undelegate(".edit-create-category", "click").delegate(".edit-create-category", "click", function () {
        var all_ok = false;
        if ($("#edit-category-name").val() == "" || $("#edit-category-name").val() == null) {
            swal("Oops", "Escriba el nombre de la categoría..!", "error");
        } else if ($(".edit-permission-select").val() == "" || $(".edit-permission-select").val() == null) {
            swal("Oops", "Seleccione los permisos..!", "error");
        } else {
            all_ok = true;
        }
        if (all_ok == true) {
            var __this = $(this);
            var postRoute = '/edit-category';
            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "json",
                data: {
                    csrfmiddlewaretoken: $(".csrfToken").val(),
                    'category_title': $("#edit-category-name").val(),
                    'permissions': JSON.stringify($(".edit-permission-select").val()),
                    'old_title': $("#old-category-name").val()
                },
            }).done(function (data) {
                if (data.success == 1) {
                    swal("Éxito!", "Categoría actualizada correctamente...!", "success")
                        .then((value) => {
                            location.reload();
                        });
                } else if (data.error == 2) {
                    swal("Oops", "La categoría ya existe..!", "error");
                } else {
                    swal("Oops", "Algo salió mal. La categoría no está actualizada...!", "error");
                }
            }).error(function (data) {
                swal("Oops", "Algo salió mal...!", "error");
            });
        }
    });

    $("body").undelegate(".editSubCategoryButton", "click").delegate(".editSubCategoryButton", "click", function () {
        $(".edit-category-select > option").each(function () {
            $(this).prop("selected", false);
        });
        $(".edit-category-select").trigger("change");
        $("#edit-subcategory-name").val($.trim($(this).parent().parent().find(".font-text600").text()));
        $("#old-subcategory-name").val($.trim($(this).parent().parent().find(".font-text600").text()));
        data = $(this).attr("data-set");
        $("#old-category-select").val(data);
        if (data) {
            $(".edit-category-select > option").each(function () {
                if ($(this).val() == $.trim(data)) {
                    $(this).prop("selected", "selected");
                }
            });
            $(".edit-category-select").trigger("change");
        }

        // Adding the main code
        $.ajax({
            type: "POST",
            url: '/get_edit_subcategory_permission',
            dataType: "json",
            data: {
                csrfmiddlewaretoken: $(".csrfToken").val(),
                'category_title': $("#subCat_Edit").val(),
                'subcategories_title': $("#edit-subcategory-name").val()
            },
        }).done(function (data) {
            console.log("Adding recv data");
            
            for(var key in data['data']) {
                let permissionData = data['data'][key]
                console.log(permissionData);

                $(".edit-sub-permission-select > option").each(function () {
                    if ($(this).val() === permissionData) {
                        $(this).prop('selected',true)
                    }
                });
            }

            $(".edit-sub-permission-select").trigger("change");
        });

    });
    $("body").undelegate(".edit-subcategory", "click").delegate(".edit-subcategory", "click", function () {
        var all_ok = false;
        if ($("#edit-subcategory-name").val() == "" || $("#edit-subcategory-name").val() == null) {
            swal("Oops", "Escriba el nombre de la subcategoría..!", "error");
        } else if ($(".edit-category-select").val() == "" || $(".edit-category-select").val() == null) {
            swal("Oops", "Seleccione una categoría..!", "error");
        } else {
            all_ok = true;
        }
        if (all_ok == true) {
            var __this = $(this);
            var postRoute = '/edit-subcategory';
            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "json",
                data: {
                    csrfmiddlewaretoken: $(".csrfToken").val(),
                    'subcategory_title': $("#edit-subcategory-name").val(),
                    'old_subcategory_title': $("#old-subcategory-name").val(),
                    'old_category_title': $("#old-category-select").val(),
                    'category_title': $(".edit-category-select").val(),
                    'permissions': JSON.stringify($(".edit-sub-permission-select").val())
                },
            }).done(function (data) {
                if (data.success == 1) {
                    swal("Éxito!", "Subcategoría actualizada correctamente...!", "success")
                        .then((value) => {
                            location.reload();
                        });
                } else if (data.error == 2) {
                    swal("Oops", "No cambiaste nada..!", "error");
                } else {
                    swal("Oops", "Algo salió mal. la subcategoría no está actualizada...!", "error");
                }
            }).error(function (data) {
                swal("Oops", "Algo salió mal...!", "error");
            });
        }
    });

    $("body").undelegate(".editFilesButton", "click").delegate(".editFilesButton", "click", function () {
        $(".subcategory_title").val($(this).attr("data-set"));
        $(".category_title").val($(this).attr("data"));
        $(".old_file").val($.trim($(this).parent().parent().find(".sub-files-name").text()));
    });

    $("#editFiles-form").on("submit", function (evt) {
        evt.preventDefault();
        var all_ok = false;
        if (0 >= $("#edit-cat-sub-files")[0].files.length) {
            swal("Oops", "Por favor seleccione archivo ..!", "error");
        } else {
            all_ok = true;
        }
        if (all_ok == true) {
            var __this = $(this);
            var postRoute = '/edit-archivo';
            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "multipart/form-data",
                data: new FormData(this),
                async: false,
                cache: false,
                contentType: false,
                processData: false,
                success: function (data) {
                    if (data.success == 1) {
                        swal("Operación realizada", "El archivo se actualizó correctamente!", "success")
                            .then((value) => {
                                location.reload();
                            });
                    } else if (data.error == 2) {
                        swal("Oops", "La categoría ya existe ..!", "error");
                    } else {
                        swal("Oops", "algo salió mal..!", "error");
                    }
                },
                error: function (data) {
                    swal("Operación realizada", "El archivo se actualizó correctamente!", "success")
                        .then((value) => {
                            location.reload();
                        });
                }
            });
        }
    });

    $("body").undelegate(".editCatFilesModal", "click").delegate(".editCatFilesModal", "click", function () {
        $(".categoryfiles").val($(this).attr("data-set"));
        $(".old_cat_file").val($.trim($(this).parent().parent().find(".cat-files-name").text()));
    });

    $("#editCatFiles-form").on("submit", function (evt) {
        evt.preventDefault();
        var all_ok = false;
        if (0 >= $("#cat-files")[0].files.length) {
            swal("Oops", "Por favor seleccione archivo ..!", "error");
        } else {
            all_ok = true;
        }
        if (all_ok == true) {
            var __this = $(this);
            var postRoute = '/edit-archivo-category-files';
            $.ajax({
                type: "POST",
                url: postRoute,
                dataType: "multipart/form-data",
                data: new FormData(this),
                async: false,
                cache: false,
                contentType: false,
                processData: false,
                success: function (data) {
                    console.log(data);
                    if (data.success == 1) {
                        swal("Operación realizada", "El archivo se actualizó correctamente!", "success")
                            .then((value) => {
                                location.reload();
                            });
                    } else if (data.error == 2) {
                        swal("Oops", "La categoría ya existe ..!", "error");
                    } else {
                        swal("Oops", "algo salió mal..!", "error");
                    }
                },
                error: function (data) {
                    swal("Operación realizada", "El archivo se actualizó correctamente!", "success")
                        .then((value) => {
                            location.reload();
                        });
                }
            });
        }
    });

    $("body").undelegate(".delete-category", "click").delegate(".delete-category", "click", function () {
        var category_title = $(this).attr("category-name")
        swal("Advertencia!", "Se eliminarán todos los archivos y carpetas de las subcategorías", "warning", {
            buttons: ["Cerrar", true],
        })
            .then((value) => {
                var postRoute = '/delete-category';

                if (value) {
                    $.ajax({
                        type: "POST",
                        url: postRoute,
                        dataType: "json",
                        data: {
                            csrfmiddlewaretoken: $(".csrfToken").val(),
                            'category_title': category_title,
                        },
                    }).done(function (data) {
                        if (data.success == 1) {
                            swal("exitosa!", "Categoría eliminada correctamente...!", "success")
                                .then((value) => {
                                    location.reload();
                                });
                        } else {
                            swal("Oops", "Algo salió mal. La categoría no se elimina...!", "error");
                        }
                    }).error(function (data) {
                        swal("Oops", "Algo salió mal...!", "error");
                    });
                }
            });
    });

    $("body").undelegate(".delete-subcategory", "click").delegate(".delete-subcategory", "click", function () {
        var category_title = $(this).attr("category-name")
        var subcategory_title = $(this).attr("subcategory-name")
        swal("Advertencia!", "¿Está seguro de que desea eliminar la subcategoría? Perderás archivos...!", "warning", {
            buttons: ["Cerrar", true],
        })
            .then((value) => {


                if (value) {
                    var postRoute = '/delete-subcategory';
                    $.ajax({
                        type: "POST",
                        url: postRoute,
                        dataType: "json",
                        data: {
                            csrfmiddlewaretoken: $(".csrfToken").val(),
                            'category_title': category_title,
                            'subcategory_title': subcategory_title,
                        },
                    }).done(function (data) {
                        if (data.success == 1) {
                            swal("Éxito!", "Subcategoría eliminada correctamente...!", "success")
                                .then((value) => {
                                    location.reload();
                                });
                        } else {
                            swal("Oops", "Algo salió mal. La subcategoría no se elimina...!", "error");
                        }
                    }).error(function (data) {
                        swal("Oops", "Algo salió mal...!", "error");
                    });
                }


            });
    });

    $("body").undelegate(".delete-category-files", "click").delegate(".delete-category-files", "click", function () {
        var category_title = $(this).attr("category-name")
        var category_file_name = $(this).attr("category_file_name")
        swal("Advertencia!", "¿Está seguro de que desea eliminar los archivos de categoría?", "warning", {
            buttons: ["Cancel", true],
        })
            .then((value) => {
                if(value) {
                    var postRoute = '/delete-category-files';
                $.ajax({
                    type: "POST",
                    url: postRoute,
                    dataType: "json",
                    data: {
                        csrfmiddlewaretoken: $(".csrfToken").val(),
                        'category_title': category_title,
                        'category_file_name': category_file_name,
                    },
                }).done(function (data) {
                    if (data.success == 1) {
                        swal("Éxito!", "Subcategoría eliminada correctamente...!", "success")
                            .then((value) => {
                                location.reload();
                            });
                    } else {
                        swal("Oops", "Algo salió mal. La subcategoría no se elimina...!", "error");
                    }
                }).error(function (data) {
                    swal("Oops", "Algo salió mal...!", "error");
                });
                }
            });
    });

    $("body").undelegate(".delete-subcategory-files", "click").delegate(".delete-subcategory-files", "click", function () {
        var category_title = $(this).attr("category-name")
        var subcategory_title = $(this).attr("sub-category-name")
        var subcategory_file_name = $(this).attr("subcategory_file_name")
        swal("Advertencia!", "¿Está seguro de que desea eliminar los archivos de subcategoría?", "warning", {
            buttons: ["Cerrar", true],
        })
            .then((value) => {
                if(value) {
                    var postRoute = '/delete-subcategory-files';
                $.ajax({
                    type: "POST",
                    url: postRoute,
                    dataType: "json",
                    data: {
                        csrfmiddlewaretoken: $(".csrfToken").val(),
                        'category_title': category_title,
                        'subcategory_title': subcategory_title,
                        'subcategory_file_name': subcategory_file_name,
                    },
                }).done(function (data) {
                    if (data.success == 1) {
                        swal("Éxito!", "Subcategoría eliminada correctamente...!", "success")
                            .then((value) => {
                                location.reload();
                            });
                    } else {
                        swal("Oops", "Algo salió mal. La subcategoría no se elimina...!", "error");
                    }
                }).error(function (data) {
                    swal("Oops", "Algo salió mal...!", "error");
                });
                }
            });
    });
});
var category;
    var subcategory;
$( function() {
    
    $('.dragable').draggable({
        revert: 'invalid'
    })

    $(".dropable").droppable({
        drop: function(event,ui) {
            category = $(this).attr('category')
            subcategory = $(this).attr('subcategory')
            filename = $(ui.draggable).attr('file_name')
            
            $.ajax({
                url: '/file/move/',
                method: 'POST',
                data: {
                    category: category,
                    subcategory: subcategory,
                    filename: filename,
                    csrfmiddlewaretoken: $(".csrfToken").val(),
                },
                success: function(data) {
                    location.reload()
                }

            })
        },
    });
});