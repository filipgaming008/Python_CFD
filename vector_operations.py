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