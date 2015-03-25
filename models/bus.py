from google.appengine.ext import db
from models.bus_route import BusRoute
from models.bus_driver import BusDriver


class Bus(db.Model):
  bus_id = db.StringProperty(default=None)
  # Defines bus's operational state.
  is_operational = db.BooleanProperty(default=False)
  # Shows whether bus is a premium, hence has altered route, etc.
  is_premium = db.BooleanProperty(default=False)
  arrival_time = db.StringProperty(default=None)
  departure_time = db.StringProperty(default=None)
  # Rework driver-bus references.
  bus_driver = db.ReferenceProperty(BusDriver)
  route = db.ReferenceProperty(BusRoute)
  

  @classmethod
  def get_by_bus_id(cls, bus_id):
    return cls.all().filter('bus_id =', bus_id).get()

 
  # @classmethod
  # def driver_assigned_once(cls, driver_id):
  # # Method to ensure each driver selected is not assigned to another bus.
  #   from models.bus import Bus
  #   driver = cls.all().filter('driver_id =', driver_id).get()
  #   buses = Bus.all()
  #   count = 0
  #   for i in range(0,len(bus_list)):
  #     if driver.key().get() == buses[i].bus_driver.key().get()
  #       count++
  #   if count > 1:
  #     return False

  def one_driver(self):
  # Returns true if and only if one driver is assigned to a bus.
  # May be unnecessary.
    if len(self.bus_driver) == 1:
      return True