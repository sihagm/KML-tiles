#This script creates a kml tile-raster according to input coordinate (upper left corner), tile size and number of tiles
import os, sys
import math

#paths
parent = os.getcwd()
parent = os.path.join(parent, '')
path = str(parent)

#___________________________________________________________________________________________________________________________________________
#user input variables - beware that in python3 you have to change raw_input to input
File_name = raw_input('Enter desired file name: ')
File_name = str(File_name)
file_kml = path+File_name+".kml"


Ystart = float(input('Enter start Lat (WGS84, decimal degrees), upper left corner: '))
Xstart = float(input('Enter start Lon (WGS84, decimal degrees), upper left corner: '))
Xspacing = int(input('Enter Lat spacing (meters): '))
Yspacing = int(input('Enter Lon spacing (meters): '))
Ynumber = int(input('Enter number of fields in Lat: '))
Ynumber = Ynumber+1
Xnumber = int(input('Enter number of fields in Lon: '))
Xnumber = Xnumber+1

#Example
# Xstart = 7.72843
# Ystart = 46.94123
# Xspacing = 100
# Yspacing = 120
# Xnumber = 10
# Xnumber = Xnumber+1
# Ynumber = 20
# Ynumber = Ynumber+1

#convert meters to degrees
m_per_deg_lon = 111132.954
radians = float(Ystart*(math.pi/180))
m_per_deg_lat = float(111139.0*math.cos(radians))

deg_per_m_lat = float(1/m_per_deg_lat)
deg_per_m_lon = float(1/m_per_deg_lon)

Xspacing = float(deg_per_m_lat*Xspacing)
Yspacing = float(deg_per_m_lon*Yspacing)


#Linestyle, color and width
#color code: Opacity-BB-GG-RR, ff0000ff = red, ffff0000 = blue, ff00ffff = yellow
color = 'ffF03214'
width = 2
width = str(width)
#size of tile names - set to 0 to only show names on the side
scale = 0.7
scale = str(scale)

#___________________________________________________________________________________________________________________________________________

#write empty kml file
f = open(file_kml, 'w')

#kml header
with open(file_kml, 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>')
    f.write('\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">')
    f.write('\n')
    f.write('<Document>')
    f.write('\n')
    f.write('<Schema name="Kachelnamen" id="Kachelnamen">')
    f.write('\n')
    f.write('  <SimpleField name="altitudeMode" type="string"></SimpleField>')
    f.write('\n')
    f.write('  <SimpleField name="tessellate" type="int"></SimpleField>')
    f.write('\n')
    f.write('  <SimpleField name="extrude" type="int"></SimpleField>')
    f.write('\n')
    f.write('  <SimpleField name="visibility" type="int"></SimpleField>')
    f.write('\n')
    f.write('  <SimpleField name="icon" type="string"></SimpleField>')
    f.write('\n')
    f.write('  <SimpleField name="snippet" type="string"></SimpleField>')
    f.write('\n')
    f.write('</Schema>')
    f.write('  <name>'+File_name+'</name>')
    f.write('\n')
    
    #write first line vertical
    f.write('  <Placemark id="vertical0">')
    f.write('\n')
    f.write('    <name>vertical0</name>')
    f.write('\n')
    f.write('    <description> </description>')
    f.write('\n')
    f.write('<Style><LineStyle><color>'+color+'</color><width>'+width+'</width></LineStyle></Style>')
    f.write('\n')
    f.write('<LineString>')
    f.write('\n')
    f.write('      <coordinates>')
    f.write('\n')
    
    Y01 = Ystart
    Y02 = Ystart-(Yspacing*(Ynumber-1))
    X01 = Xstart
    X02 = X01
    
    Y01i = str(Y01)
    Y02i = str(Y02)
    X01i = str(X01)
    X02i = str(X02)
    
    f.write(X01i+","+Y01i)
    f.write('\n')
    f.write(X02i+","+Y02i)   
    
    f.write('\n')
    f.write('      </coordinates>')
    f.write('\n')
    f.write('      <altitudeMode>clampToGround</altitudeMode>')
    f.write('\n')
    f.write('    </LineString>')
    f.write('\n')
    f.write('  </Placemark>')
    f.write('\n') 
    
    
    #write first line horizontal
    f.write('  <Placemark id="horizontal0">')
    f.write('\n')
    f.write('    <name>horizontal0</name>')
    f.write('\n')
    f.write('    <description> </description>')
    f.write('\n')
    f.write('<Style><LineStyle><color>'+color+'</color><width>'+width+'</width></LineStyle></Style>')
    f.write('\n')
    f.write('<LineString>')
    f.write('\n')
    f.write('      <coordinates>')
    f.write('\n')
    
    X01 = Xstart
    X02 = Xstart+(Xspacing*(Xnumber-1))
    Y01 = Ystart
    Y02 = Y01
    
    Y01i = str(Y01)
    Y02i = str(Y02)
    X01i = str(X01)
    X02i = str(X02)
    
    f.write(X01i+","+Y01i)
    f.write('\n')
    f.write(X02i+","+Y02i)   
    
    f.write('\n')
    f.write('      </coordinates>')
    f.write('\n')
    f.write('      <altitudeMode>clampToGround</altitudeMode>')
    f.write('\n')
    f.write('    </LineString>')
    f.write('\n')
    f.write('  </Placemark>')
    f.write('\n') 
        
    
    #write the lines
    for i in range(1, Xnumber):
    
        #create vertical lines ------------------------------------------------------------------------
        Linename_aux = i
        Linename = "vertical"+str(Linename_aux)
        f.write("  <Placemark id="+'"'+Linename+'"'+">")
        f.write('\n')
        f.write('    <name>'+Linename+'</name>')
        f.write('\n')
        f.write('    <description> </description>')
        f.write('\n')
        f.write('<Style><LineStyle><color>'+color+'</color><width>'+width+'</width></LineStyle></Style>')
        f.write('\n')
        f.write('<LineString>')
        f.write('\n')
        f.write('      <coordinates>')
        f.write('\n')
        
        
        Y1 = Ystart
        Y2 = Ystart-(Yspacing*(Ynumber-1))
        X1 = Xstart+(Xspacing*i)
        X2 = X1
        
        Y1i = str(Y1)
        Y2i = str(Y2)
        X1i = str(X1)
        X2i = str(X2)

        #write coords
        f.write(X1i+","+Y1i)
        f.write('\n')
        f.write(X2i+","+Y2i)        
        
        f.write('\n')
        f.write('      </coordinates>')
        f.write('\n')
        f.write('      <altitudeMode>clampToGround</altitudeMode>')
        f.write('\n')
        f.write('    </LineString>')
        f.write('\n')
        f.write('  </Placemark>')
        f.write('\n')
        
        #create horizontal side labels
        K_name = str(i)
        f.write('<Placemark>')
        f.write('\n')
        f.write('<name>'+K_name+'</name>')
        f.write('\n')
        f.write('<description> </description>')
        f.write('\n')
        f.write('<Style><IconStyle><color>00000000</color><scale>0</scale></IconStyle><LabelStyle><color>'+color+'</color><scale>1</scale></LabelStyle></Style>')
        f.write('\n')
        f.write('<ExtendedData><SchemaData schemaUrl="#Kachelnamen">')
        f.write('\n')
        f.write('<SimpleData name="altitudeMode">clampToGround</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="tessellate">-1</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="extrude">0</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="visibility">-1</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="snippet"></SimpleData>')
        f.write('\n')
        f.write('</SchemaData></ExtendedData>')
        f.write('\n')
        
        YK = Ystart
        XK = (Xstart-(Xspacing/2))+(Xspacing*i)
        YKi = str(YK)
        XKi = str(XK)
        
        f.write('<Point><coordinates>')
        f.write(XKi+","+YKi)
        f.write('</coordinates></Point>')
        f.write('\n')
        f.write('</Placemark>')
        f.write('\n')
        #----------------------------------------------------------------------------------------------
        #create tile-names
        for i2 in range(1, Ynumber):
            K_name1 = str(i)
            K_name2 = str(chr(i2+64))
            K_name = K_name2+K_name1
            f.write('<Placemark>')
            f.write('\n')
            f.write('<name>'+K_name+'</name>')
            f.write('\n')
            f.write('<description> </description>')
            f.write('\n')
            f.write('<Style><IconStyle><color>00000000</color><scale>0</scale></IconStyle><LabelStyle><color>'+color+'</color><scale>'+scale+'</scale></LabelStyle></Style>')
            f.write('\n')
            f.write('<ExtendedData><SchemaData schemaUrl="#Kachelnamen">')
            f.write('\n')
            f.write('<SimpleData name="altitudeMode">clampToGround</SimpleData>')
            f.write('\n')
            f.write('<SimpleData name="tessellate">-1</SimpleData>')
            f.write('\n')
            f.write('<SimpleData name="extrude">0</SimpleData>')
            f.write('\n')
            f.write('<SimpleData name="visibility">-1</SimpleData>')
            f.write('\n')
            f.write('<SimpleData name="snippet"></SimpleData>')
            f.write('\n')
            f.write('</SchemaData></ExtendedData>')
            f.write('\n')
            
            YK = (Ystart+(Yspacing/2))-(Yspacing*i2)
            XK = (Xstart-(Xspacing/2))+(Xspacing*i)
            
            YKi = str(YK)
            XKi = str(XK)
            
            f.write('<Point><coordinates>')
            f.write(XKi+","+YKi)
            f.write('</coordinates></Point>')
            f.write('\n')
            f.write('</Placemark>')
            f.write('\n')

        
        
        
        
        
    for i in range(1, Ynumber):
        Linename_aux = i
        #create horizontal lines ---------------------------------------------------------------------
        Linename2 = "horizontal"+str(Linename_aux)
        f.write("  <Placemark id="+'"'+Linename2+'"'+">")
        f.write('\n')
        f.write('    <name>'+Linename2+'</name>')
        f.write('\n')
        f.write('    <description> </description>')
        f.write('\n')
        f.write('<Style><LineStyle><color>'+color+'</color><width>'+width+'</width></LineStyle></Style>')
        f.write('\n')
        f.write('<LineString>')
        f.write('\n')
        f.write('      <coordinates>')
        f.write('\n')
        
        
        X3 = Xstart
        X4 = Xstart+(Xspacing*(Xnumber-1))
        Y3 = Ystart-(Yspacing*i)
        Y4 = Y3
         
        
        Y3i = str(Y3)
        Y4i = str(Y4)
        X3i = str(X3)
        X4i = str(X4)

        #write coords
        f.write(X3i+","+Y3i)
        f.write('\n')
        f.write(X4i+","+Y4i)        
        
        f.write('\n')
        f.write('      </coordinates>')
        f.write('\n')
        f.write('      <altitudeMode>clampToGround</altitudeMode>')
        f.write('\n')
        f.write('    </LineString>')
        f.write('\n')
        f.write('  </Placemark>')
        f.write('\n')
        
        #create vertical side labels
        K_name2 = str(chr(i+64))
        f.write('<Placemark>')
        f.write('\n')
        f.write('<name>'+K_name2+'</name>')
        f.write('\n')
        f.write('<description> </description>')
        f.write('\n')
        f.write('<Style><IconStyle><color>00000000</color><scale>0</scale></IconStyle><LabelStyle><color>'+color+'</color><scale>1</scale></LabelStyle></Style>')
        f.write('\n')
        f.write('<ExtendedData><SchemaData schemaUrl="#Kachelnamen">')
        f.write('\n')
        f.write('<SimpleData name="altitudeMode">clampToGround</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="tessellate">-1</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="extrude">0</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="visibility">-1</SimpleData>')
        f.write('\n')
        f.write('<SimpleData name="snippet"></SimpleData>')
        f.write('\n')
        f.write('</SchemaData></ExtendedData>')
        f.write('\n')
        
        XK = Xstart
        YK = (Ystart+(Yspacing/2))-(Yspacing*i)
        YKi = str(YK)
        XKi = str(XK)
        
        f.write('<Point><coordinates>')
        f.write(XKi+","+YKi)
        f.write('</coordinates></Point>')
        f.write('\n')
        f.write('</Placemark>')
        f.write('\n')        
         
        
    # #write kml ending
    f.write('</Document>')
    f.write('\n')
    f.write('</kml>')

    f.close()




input('DONE ----- Press ENTER to exit')