libraries <- c('devtools',
                'sp',
                'spdep',
                'rgdal', 
                'raster',
                'maptools',
                'mapview',
                'spatstat',
                'gstat', 
                'reshape2',
                'magrittr',
                'dplyr',
                'mgcv',
                'INLA',
                'brinla',
                'INLAutils')
CheckInstallPackages <- function(pkgs){

#For each pkg in pkgs (attempt to load each package one at a time):

 x <- lapply(pkgs, function(pkg){

  #Load the package if available,

  if(!do.call("require", list(pkg))) {

   #Silently attempt to install into the default library

    if(pkg=='INLA'){
            install.packages('INLA', repos=c(getOption("repos"), INLA="https://inla.r-inla-download.org/R/stable"), dep=TRUE)
    }
    if(pkg=='brinla'){
        install_github("julianfaraway/brinla")
    }
    if(pkg=='INLAutils'){
        install_github('timcdlucas/INLAutils', dep = FALSE)
    }      
      
   try(install.packages(pkg, lib=.Library,repos="http://cran.rstudio.com"))

   #Now attempt to load the package, catch error if it wasn't installed

   tryCatch(do.call("library", list(pkg)),

    #Catch if we're unable to install into the default library

    error = function(err) {

    #If non-interactive, install into this user's personal library

    if(!interactive()) {

        #Get the path to this user's personal library

        personalLibPath <- Sys.getenv("R_LIBS_USER")

        #If the personal library is not in the list of libraries

        if(is.na(match(personalLibPath, .libPaths()))) {

        #Then create the personal library

        dir.create(personalLibPath, recursive = TRUE)
        #And add the personal library to the list of libraries

        .libPaths(personalLibPath)

    }

    #Attempt to install the package into the personal library

    #If this fails, raise the error back to the report

    install.packages(pkg, lib=personalLibPath, repos="http://cran.rstudio.com")
    
    #Finally, attempt to load the package

    do.call("library", list(pkg))

 }})}})

}

CheckInstallPackages(libraries)