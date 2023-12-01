# imports
import math

# class def
class vector_operation():
    
    # addition operation
    def add(a, b):
        
        a_x, a_y = a[0], a[1]
        b_x, b_y = b[0], b[1]

        m_x, m_y = a_x + b_x, a_y + b_y

        m = [m_x, m_y]

        return m

    # subtraction operation
    def sub(a, b):

        a_x, a_y = a[0], a[1]
        b_x, b_y = b[0], b[1]

        m_x, m_y = a_x - b_x, a_y - b_y

        m = [m_x, m_y]

        return m

    # multiplication operation
    def mult(a, b):

        a_x, a_y = a[0], a[1]
        b_x, b_y = b[0], b[1]

        m_x, m_y = a_x * b_x, a_y * b_y

        m = [m_x, m_y]

        return m

    # division operation
    def div(a, b):

        a_x, a_y = a[0], a[1]
        b_x, b_y = b[0], b[1]

        m_x, m_y = a_x / b_x, a_y / b_y

        m = [m_x, m_y]

        return m

    # exponent operation
    def pow(a, b):

        a_x, a_y = a[0], a[1]
        b_x, b_y = b[0], b[1]

        m_x, m_y = math.pow(a_x, b_x), math.pow(a_y, b_y)

        m = [m_x, m_y]

        return m

    # carthesian to polar
    def cart2pol(b):
        
        x = b[0]
        y = b[1]
        
        rho = math.sqrt(x**2 + y**2)
        phi = math.degrees(math.atan2(y, x))

        m = [rho, phi]

        return(m)

    # polar to carthesian
    def pol2cart(b):
        
        rho = b[0]
        phi = b[1]

        x = rho * math.cos(math.radians(phi))
        y = rho * math.sin(math.radians(phi))

        m = [x, y]

        return(m)

    # distance
    def distance(a, b):

        a_x, a_y = a[0], a[1]
        b_x, b_y = b[0], b[1]

        distance = math.sqrt((b_x - a_x)**2 + (b_y - a_y)**2)