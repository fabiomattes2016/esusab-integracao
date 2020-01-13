#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import br.gov.saude.esusab.ras.common.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class FichaVisitaDomiciliarChildThrift:
  """
  Attributes:
   - turno
   - numProntuario
   - cnsCidadao
   - dtNascimento
   - sexo
   - statusVisitaCompartilhadaOutroProfissional
   - motivosVisita
   - desfecho
   - microArea
   - stForaArea
   - tipoDeImovel
   - pesoAcompanhamentoNutricional
   - alturaAcompanhamentoNutricional
   - cpfCidadao
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'turno', None, None, ), # 1
    (2, TType.STRING, 'numProntuario', None, None, ), # 2
    (3, TType.STRING, 'cnsCidadao', None, None, ), # 3
    (4, TType.I64, 'dtNascimento', None, None, ), # 4
    (5, TType.I64, 'sexo', None, None, ), # 5
    (6, TType.BOOL, 'statusVisitaCompartilhadaOutroProfissional', None, None, ), # 6
    (7, TType.LIST, 'motivosVisita', (TType.I64,None), None, ), # 7
    (8, TType.I64, 'desfecho', None, None, ), # 8
    (9, TType.STRING, 'microArea', None, None, ), # 9
    (10, TType.BOOL, 'stForaArea', None, None, ), # 10
    (11, TType.I64, 'tipoDeImovel', None, None, ), # 11
    (12, TType.DOUBLE, 'pesoAcompanhamentoNutricional', None, None, ), # 12
    (13, TType.DOUBLE, 'alturaAcompanhamentoNutricional', None, None, ), # 13
    (14, TType.STRING, 'cpfCidadao', None, None, ), # 14
  )

  def __init__(self, turno=None, numProntuario=None, cnsCidadao=None, dtNascimento=None, sexo=None, statusVisitaCompartilhadaOutroProfissional=None, motivosVisita=None, desfecho=None, microArea=None, stForaArea=None, tipoDeImovel=None, pesoAcompanhamentoNutricional=None, alturaAcompanhamentoNutricional=None, cpfCidadao=None,):
    self.turno = turno
    self.numProntuario = numProntuario
    self.cnsCidadao = cnsCidadao
    self.dtNascimento = dtNascimento
    self.sexo = sexo
    self.statusVisitaCompartilhadaOutroProfissional = statusVisitaCompartilhadaOutroProfissional
    self.motivosVisita = motivosVisita
    self.desfecho = desfecho
    self.microArea = microArea
    self.stForaArea = stForaArea
    self.tipoDeImovel = tipoDeImovel
    self.pesoAcompanhamentoNutricional = pesoAcompanhamentoNutricional
    self.alturaAcompanhamentoNutricional = alturaAcompanhamentoNutricional
    self.cpfCidadao = cpfCidadao

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.turno = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.numProntuario = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.cnsCidadao = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.dtNascimento = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.sexo = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BOOL:
          self.statusVisitaCompartilhadaOutroProfissional = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.motivosVisita = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI64()
            self.motivosVisita.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.desfecho = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.microArea = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.BOOL:
          self.stForaArea = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I64:
          self.tipoDeImovel = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.DOUBLE:
          self.pesoAcompanhamentoNutricional = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.DOUBLE:
          self.alturaAcompanhamentoNutricional = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.cpfCidadao = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FichaVisitaDomiciliarChildThrift')
    if self.turno is not None:
      oprot.writeFieldBegin('turno', TType.I64, 1)
      oprot.writeI64(self.turno)
      oprot.writeFieldEnd()
    if self.numProntuario is not None:
      oprot.writeFieldBegin('numProntuario', TType.STRING, 2)
      oprot.writeString(self.numProntuario)
      oprot.writeFieldEnd()
    if self.cnsCidadao is not None:
      oprot.writeFieldBegin('cnsCidadao', TType.STRING, 3)
      oprot.writeString(self.cnsCidadao)
      oprot.writeFieldEnd()
    if self.dtNascimento is not None:
      oprot.writeFieldBegin('dtNascimento', TType.I64, 4)
      oprot.writeI64(self.dtNascimento)
      oprot.writeFieldEnd()
    if self.sexo is not None:
      oprot.writeFieldBegin('sexo', TType.I64, 5)
      oprot.writeI64(self.sexo)
      oprot.writeFieldEnd()
    if self.statusVisitaCompartilhadaOutroProfissional is not None:
      oprot.writeFieldBegin('statusVisitaCompartilhadaOutroProfissional', TType.BOOL, 6)
      oprot.writeBool(self.statusVisitaCompartilhadaOutroProfissional)
      oprot.writeFieldEnd()
    if self.motivosVisita is not None:
      oprot.writeFieldBegin('motivosVisita', TType.LIST, 7)
      oprot.writeListBegin(TType.I64, len(self.motivosVisita))
      for iter6 in self.motivosVisita:
        oprot.writeI64(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.desfecho is not None:
      oprot.writeFieldBegin('desfecho', TType.I64, 8)
      oprot.writeI64(self.desfecho)
      oprot.writeFieldEnd()
    if self.microArea is not None:
      oprot.writeFieldBegin('microArea', TType.STRING, 9)
      oprot.writeString(self.microArea)
      oprot.writeFieldEnd()
    if self.stForaArea is not None:
      oprot.writeFieldBegin('stForaArea', TType.BOOL, 10)
      oprot.writeBool(self.stForaArea)
      oprot.writeFieldEnd()
    if self.tipoDeImovel is not None:
      oprot.writeFieldBegin('tipoDeImovel', TType.I64, 11)
      oprot.writeI64(self.tipoDeImovel)
      oprot.writeFieldEnd()
    if self.pesoAcompanhamentoNutricional is not None:
      oprot.writeFieldBegin('pesoAcompanhamentoNutricional', TType.DOUBLE, 12)
      oprot.writeDouble(self.pesoAcompanhamentoNutricional)
      oprot.writeFieldEnd()
    if self.alturaAcompanhamentoNutricional is not None:
      oprot.writeFieldBegin('alturaAcompanhamentoNutricional', TType.DOUBLE, 13)
      oprot.writeDouble(self.alturaAcompanhamentoNutricional)
      oprot.writeFieldEnd()
    if self.cpfCidadao is not None:
      oprot.writeFieldBegin('cpfCidadao', TType.STRING, 14)
      oprot.writeString(self.cpfCidadao)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.turno)
    value = (value * 31) ^ hash(self.numProntuario)
    value = (value * 31) ^ hash(self.cnsCidadao)
    value = (value * 31) ^ hash(self.dtNascimento)
    value = (value * 31) ^ hash(self.sexo)
    value = (value * 31) ^ hash(self.statusVisitaCompartilhadaOutroProfissional)
    value = (value * 31) ^ hash(self.motivosVisita)
    value = (value * 31) ^ hash(self.desfecho)
    value = (value * 31) ^ hash(self.microArea)
    value = (value * 31) ^ hash(self.stForaArea)
    value = (value * 31) ^ hash(self.tipoDeImovel)
    value = (value * 31) ^ hash(self.pesoAcompanhamentoNutricional)
    value = (value * 31) ^ hash(self.alturaAcompanhamentoNutricional)
    value = (value * 31) ^ hash(self.cpfCidadao)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class FichaVisitaDomiciliarMasterThrift:
  """
  Attributes:
   - uuidFicha
   - tpCdsOrigem
   - headerTransport
   - visitasDomiciliares
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuidFicha', None, None, ), # 1
    (2, TType.I32, 'tpCdsOrigem', None, None, ), # 2
    (3, TType.STRUCT, 'headerTransport', (br.gov.saude.esusab.ras.common.ttypes.UnicaLotacaoHeaderThrift, br.gov.saude.esusab.ras.common.ttypes.UnicaLotacaoHeaderThrift.thrift_spec), None, ), # 3
    (4, TType.LIST, 'visitasDomiciliares', (TType.STRUCT,(FichaVisitaDomiciliarChildThrift, FichaVisitaDomiciliarChildThrift.thrift_spec)), None, ), # 4
  )

  def __init__(self, uuidFicha=None, tpCdsOrigem=None, headerTransport=None, visitasDomiciliares=None,):
    self.uuidFicha = uuidFicha
    self.tpCdsOrigem = tpCdsOrigem
    self.headerTransport = headerTransport
    self.visitasDomiciliares = visitasDomiciliares

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuidFicha = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.tpCdsOrigem = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.headerTransport = br.gov.saude.esusab.ras.common.ttypes.UnicaLotacaoHeaderThrift()
          self.headerTransport.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.visitasDomiciliares = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = FichaVisitaDomiciliarChildThrift()
            _elem12.read(iprot)
            self.visitasDomiciliares.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FichaVisitaDomiciliarMasterThrift')
    if self.uuidFicha is not None:
      oprot.writeFieldBegin('uuidFicha', TType.STRING, 1)
      oprot.writeString(self.uuidFicha)
      oprot.writeFieldEnd()
    if self.tpCdsOrigem is not None:
      oprot.writeFieldBegin('tpCdsOrigem', TType.I32, 2)
      oprot.writeI32(self.tpCdsOrigem)
      oprot.writeFieldEnd()
    if self.headerTransport is not None:
      oprot.writeFieldBegin('headerTransport', TType.STRUCT, 3)
      self.headerTransport.write(oprot)
      oprot.writeFieldEnd()
    if self.visitasDomiciliares is not None:
      oprot.writeFieldBegin('visitasDomiciliares', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.visitasDomiciliares))
      for iter13 in self.visitasDomiciliares:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuidFicha is None:
      raise TProtocol.TProtocolException(message='Required field uuidFicha is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uuidFicha)
    value = (value * 31) ^ hash(self.tpCdsOrigem)
    value = (value * 31) ^ hash(self.headerTransport)
    value = (value * 31) ^ hash(self.visitasDomiciliares)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
