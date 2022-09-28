#! /usr/bin/env python3
#
def sphere_fibonacci_grid_display ( ng, xg, filename ):

#*****************************************************************************80
#
## SPHERE_FIBONACCI_GRID_DISPLAY displays a Fibonacci grid on a sphere.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NG, the number of grid points.
#
#    Input, real XG(3,NG), the coordinates of the grid points.
#
#    Input, string FILENAME, the name of the output file.
#
  import matplotlib.pyplot as plt
  import numpy as np
  from mpl_toolkits.mplot3d import Axes3D

  fig = plt.figure ( )
  ax = fig.add_subplot ( 111, projection = '3d' )
#
#  Draw the grid points.
#
  ax.scatter ( xg[:,0], xg[:,1], xg[:,2], 'b' )

  ax.set_xlabel ( '<---X--->' )
  ax.set_ylabel ( '<---Y--->' )
  ax.set_zlabel ( '<---Z--->' )
  ax.set_title ( 'Fibonacci spiral on sphere' )
  ax.grid ( True )
# ax.axis ( 'equal' )

# plt.show ( block = False )
  print ( '  Graphics saved as "', filename, '"' )
  plt.show()
  plt.savefig ( filename )

  plt.clf ( )

  return

def sphere_fibonacci_grid_display_test ( ):

#*****************************************************************************80
#
#% SPHERE_FIBONACCI_GRID_DISPLAY_TEST tests SPHERE_FIBONACCI_GRID_DISPLAY.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPHERE_FIBONACCI_GRID_DISPLAY_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SPHERE_FIBONACCI_GRID_DISPLAY displays points on a sphere' )
  print ( '  that lie on a Fibonacci spiral.' )

  ng = 400
  print ( '' )
  print ( '  Number of points NG = %d' % ( ng ) )

  xg = sphere_fibonacci_grid_points ( ng )
#
#  Display the nodes.
#
  filename = 'sphere_fibonacci_grid_display.png'

  sphere_fibonacci_grid_display ( ng, xg, filename )

  print ( '' )
  print ( '  Plot saved to file "%s".' % ( filename ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPHERE_FIBONACCI_GRID_DISPLAY_TEST:' )
  print ( '  Normal end of execution.' )
  return

def sphere_fibonacci_grid_points ( ng ):

#*****************************************************************************80
#
## SPHERE_FIBONACCI_GRID_POINTS: Fibonacci spiral gridpoints on a sphere.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 May 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Richard Swinbank, James Purser,
#    Fibonacci grids: A novel approach to global modelling,
#    Quarterly Journal of the Royal Meteorological Society,
#    Volume 132, Number 619, July 2006 Part B, pages 1769-1793.
#
#  Parameters:
#
#    Input, integer NG, the number of points.
#
#    Output, real XG(3,N), the grid points.
#
  import numpy as np

  phi = ( 1.0 + np.sqrt ( 5.0 ) ) / 2.0

  theta = np.zeros ( ng )
  sphi = np.zeros ( ng )
  cphi = np.zeros ( ng )

  with open('fibonacci-theta-sphi-cphi.txt', 'w') as fc:
      for i in range ( 0, ng ):
          i2 = 2 * i - ( ng - 1 )
          theta[i] = 2.0 * np.pi * float ( i2 ) / phi
          sphi[i] = float ( i2 ) / float ( ng )
          cphi[i] = np.sqrt ( float ( ng + i2 ) * float ( ng - i2 ) ) / float ( ng )
          ftsc = str(theta[i]) + '\t' + str(sphi[i]) + '\t' + '\t' + str(cphi[i])
          fc.write(ftsc)
          fc.write('\n')
                    
    #print ('values for :', i)
    #print (i2)
    #print (theta[i], "\t", sphi[i], "\t", cphi[i])

  xg = np.zeros ( ( ng, 3 ) )
  xg_sum = np.zeros(3)
  with open('spherical-fibonacci-grid-points.xyz', 'w') as fw:
      for i in range ( 0, ng ) :
          xg[i,0] = cphi[i] * np.sin ( theta[i] )
          xg[i,1] = cphi[i] * np.cos ( theta[i] )
          xg[i,2] = sphi[i]
          tsc = str(xg[i,0]) + '\t' + str(xg[i, 1]) + '\t' + str(xg[i, 2])
          fw.write(tsc)
          fw.write('\n')
      
#      xg_sum = (np.sum(xg, axis=0))
#      xg = xg - xg_sum
  
  with open('fibonacci-400-grid-points.txt', 'w') as fbw:
      for coor in xg:
          rho = sum(coor**2)**0.5
          theta = np.arccos(coor[2]/rho)
          phi = np.arctan2(coor[1], coor[0])
          frtp = str(theta) + '\t' + str(phi) + '\t' + str(rho)
          fbw.write(frtp)
          fbw.write('\n')


  return xg

"""
def sphere_fibonacci_grid_points_test ( ):

#*****************************************************************************80
#
#% SPHERE_FIBONACCI_GRID_POINTS_TEST tests SPHERE_FIBONACCI_GRID_POINTS.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPHERE_FIBONACCI_GRID_POINTS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  SPHERE_FIBONACCI_GRID_POINTS computes points on a sphere' )
  print ( '  that lie on a Fibonacci spiral.' )

  ng = 400
  print ( '' )
  print ( '  Number of points NG = %d' % ( ng ) )

  xg = sphere_fibonacci_grid_points ( ng )

  #r8mat_print_some ( ng, 3, xg, 0, 0, 19, 2, '  Part of the grid array:' )
#
#  Write the nodes to a file.
#
  #filename = 'sphere_fibonacci_grid_points.xyz'

  #r8mat_write ( filename, ng, 3, xg )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPHERE_FIBONACCI_GRID_POINTS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def sphere_fibonacci_grid_test ( ):

#*****************************************************************************80
#
## SPHERE_FIBONACCI_GRID_TEST tests the SPHERE_FIBONACCI_GRID library.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    15 May 2015
#
#  Author:
#
#    John Burkardt
#
  import platform

  print ( '' )
  print ( 'SPHERE_FIBONACCI_GRID_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  Test the SPHERE_FIBONACCI_GRID library.' )
#
#  Utilities:
#
  r8mat_print_test ( )
  r8mat_print_some_test ( )
  r8mat_write_test ( )
  timestamp_test ( )
#
#  Library.
#
  sphere_fibonacci_grid_points_test ( )
  sphere_fibonacci_grid_display_test ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'SPHERE_FIBONACCI_GRID_TEST:' )
  print ( '  Normal end of execution.' )
  return
"""
def timestamp ( ):

#*****************************************************************************80
#
## TIMESTAMP prints the date as a timestamp.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    06 April 2013
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import time

  t = time.time ( )
  print ( time.ctime ( t ) )

  return None

def timestamp_test ( ):

#*****************************************************************************80
#
## TIMESTAMP_TEST tests TIMESTAMP.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license. 
#
#  Modified:
#
#    03 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    None
#
  import platform

  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  TIMESTAMP prints a timestamp of the current date and time.' )
  print ( '' )

  timestamp ( )
#
#  Terminate.
#
  print ( '' )
  print ( 'TIMESTAMP_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  timestamp ( )
  sphere_fibonacci_grid_display_test( )
  timestamp ( )

